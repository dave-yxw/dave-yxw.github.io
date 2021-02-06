# %(day)02d 日结单

{%% include  templates/daily_report.liquid jdata=site.data.daily_report.%(broker_name)s_%(account_id)d_%(year)d%(month)02d%(day)02d %%}