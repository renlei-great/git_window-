import datetime
import time

from jqdatasdk import *

auth('18846444159', 'aA1192338674')

end_t = time.time()
# start_t = time.time() - 24 * 60 * 60
start_t = time.time() - 365 * 24 * 60 * 60
end_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_t))
start_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_t))
print(f'开始时间:{start_date} - 结束时间:{end_date} 所有A股实时价格')
print('天-------------------')
df = get_price(
        security='000018.XSHE',
        start_date=start_date,
        end_date=end_date,
        # count=3,
        frequency='daily',  # daily minute
    )
for index, row in df.iterrows():
    # if any([str(df['close'].values[0]) == 'nan',str(df['open'].values[0]) == 'nan',str(df['high'].values[0]) == 'nan',
    #         str(df['low'].values[0]) == 'nan',str(df['volume'].values[0]) == 'nan',]):
    #     print(row.close, type(row.close))
    # a = str(row.close)
    # print(row.close, a)
    # print(type(a))
    print(row)


a = {1:1, 2:2, 3:3}
for i, j in a.items():
    print(i, j)
# df = 0
# for i in range(10):
#     if i == 3:
#         df = 1
# print(df)
#
# print(df)
# print('分钟-------------------')
# dfm = get_price(
#         security='000001.XSHE',
#         start_date=start_date,
#         end_date=end_date,
#         frequency='minute',  # daily minute
#     )
#
# print(dfm)