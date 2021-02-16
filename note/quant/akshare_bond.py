import akshare as ak
# https://www.akshare.xyz/zh_CN/latest/
import pandas as pd

bond_zh_cov_df = ak.bond_zh_cov()
bond_code_l = bond_zh_cov_df['交易场所'].map(lambda p: p[-2:].lower()) + bond_zh_cov_df['债券代码']


def getBondFirstPrice(bond_code):
    # 有些新浪没数据
    try:
        return ak.bond_zh_hs_cov_daily(symbol=bond_code).iloc[0]
    except:
        return {"open":None, "high":None, "low":None, "close": None, "volume": None}

bond_first_day_price = pd.DataFrame(bond_code_l.map(getBondFirstPrice).to_list())
bond_first_day_price = pd.concat([bond_zh_cov_df, bond_first_day_price], axis=1).to_csv("bond_first_day_price.csv")
