import os
import pandas as pd
import json

# 程序功能说明：查看daily_report目录下文件，和account的历史文件，对比生成对应的daily/month/year.md文件

daily_report_dir = "_data/daily_report/"
account_hist_dir = "_data/account_hist/"

day_report_tpl = open("_includes/templates/daily_report.md.tpl", encoding="utf8").read()
month_tpl = open("_includes/templates/readme_month.md.tpl", encoding="utf8").read()
year_tpl = open("_includes/templates/readme_year.md.tpl", encoding="utf8").read()
account_tpl = open("_includes/templates/readme_account.md.tpl", encoding="utf8").read()

# 读取daily_report文件列表
daily_report_files = pd.DataFrame([[f]+f.split(".")[0].split("_") for f in os.listdir(daily_report_dir)
                                   if f.endswith(".json")],
                                  columns=["file", "broker_name", "account_id", "date"])
daily_report_files['broker_account'] = daily_report_files['broker_name']+"_"+daily_report_files['account_id']

# 对出现过的broker_name, account_id, 读取已有的历史数据。初始时没有历史数据
account_list = daily_report_files["broker_account"].drop_duplicates()
hist_columns = ['date', 'balance', 'margin', 'equity', 'open_return', 'closed_return', 'update_time']


def create_dir(p, c):
    if not os.path.exists(p):
        os.mkdir(p)
        open(p+"README.md", "w", encoding="utf8").write(c)


for broker_account in account_list:
    config = {}
    config['broker_name'], account_id = broker_account.split("_")
    config['account_id'] = int(account_id)

    # read hist
    hist_file = account_hist_dir+broker_account+".csv"
    account_all_f = daily_report_files[daily_report_files.broker_account == broker_account]
    need_merge = True
    if os.path.exists(hist_file):
        account_hist_d = pd.read_csv(hist_file)
        account_hist_d['date'] = account_hist_d['date'].map(str)
        # 剔除已经存在的date
        merge_d = account_all_f.merge(account_hist_d.date, on='date', how="left", indicator=True)
        new_f = merge_d[merge_d["_merge"] == "left_only"]
    else:
        account_hist_d = None
        need_merge = False
        new_f = account_all_f

    # 读取所有新的数据
    new_d = []
    for idx, row in new_f.iterrows():
        f = row['file']
        json_d = json.load(open(daily_report_dir+f))
        daily_d = json_d['account']
        daily_d['date'] = row['date']  # 20210102, 与json中格式不同
        for k in ['open_return', 'closed_return', 'update_time']:
            daily_d[k] = json_d[k]
        new_d.append(daily_d)
    if len(new_d) == 0:  # 没有新数据
        continue
    new_d = pd.DataFrame(new_d)[hist_columns].sort_values(by='date')

    # 合并老数据，并写入csv. todo: 文件全量写入 --> 增量写入
    total_d = new_d
    if need_merge:
        total_d = pd.concat([account_hist_d, new_d]).sort_values(by='date')
    total_d.to_csv(hist_file, header=True, index=None)

    # 生成目录并写入目录的readme
    p = "mt_report/%(broker_name)s_%(account_id)s/" % config
    create_dir(p, account_tpl % config)

    # 对每个date，生成对应的daily md文件
    for date in new_d['date']:
        config['date'] = date
        config['year'] = int(date[:4])
        config['month'] = int(date[4:6])
        config['day'] = int(date[6:])
        create_dir(p+"/%(year)d/" % config, year_tpl % config)
        create_dir(p+"/%(year)d/%(month)02d/" % config, month_tpl % config)
        daily_md_target_f = p+"/%(year)d/%(month)02d/%(day)02d.md" % config
        open(daily_md_target_f, 'w', encoding='utf8').write(day_report_tpl % config)

    # 年度readme.md用到的数据
    # 从total_d中采集完整数据
    # 纯交易利润，剔除了出入金的问题
    total_d['profit'] = total_d['closed_return'] + total_d['open_return'] - total_d['open_return'].shift(1).fillna(0)
    total_d['date'] = pd.to_datetime(total_d['date']).map(lambda t: t.tz_localize(tz='Asia/Shanghai'))   # todo, timezone=utc?
    total_d['year'] = total_d.date.map(lambda d: d.year)
    years = set(pd.to_datetime(new_d.date).map(lambda d: d.year).drop_duplicates())
    for year in years:
        config['year'] = year
        year_d = total_d[['date', 'balance', 'equity', 'profit']][total_d['year'] == year]
        init_equity = year_d.iloc[0]
        init_equity = init_equity['equity'] - init_equity['profit']
        year_d['prifit_ratio'] = year_d['profit'] / init_equity * 100
        year_d['cum_profit'] = year_d['profit'].cumsum()
        year_d['cum_profit_ratio'] = year_d['cum_profit']/init_equity * 100
        # 以json格式输出到年度的文件目录下, todo: date的格式需要与echarts协调好，格式，文件地址

        # open(p + "/%(year)d/equity_hist.json" % config, "w", encoding='utf8')\
        #     .write(year_d.to_json(orient="split", index=False).replace("],", "],\n"))
        year_d.to_json(p + "/%(year)d/equity_hist.json" % config, orient='split')
