import csv
import hashlib
import time
import datetime

from jqdatasdk import *
import psycopg2

auth('18846444159', 'aA1192338674')

# config--------
REMOTE_DATABASE = 'renlei_test'
REMOTE_USER = 'postgres'
REMOTE_PORT = '52344'
REMOTE_HOST = 'localhost'
REMOTE_PASSWORD = 'renlei'


# 生成bar数据唯一ID
def hash_sha3_256_bar(assets_id,  timestamp):
    b = assets_id + str(timestamp)
    c = bytes(b, 'utf-8')
    x = hashlib.sha3_256()
    x.update(c)
    return x.hexdigest()


# 获取昨天同一时期的close_price
def get_yesterday_meanwhile_data(assets_id, current_str_time):
    # 获得各个时期的时间戳
    current_time = int(datetime.datetime.strptime(current_str_time, "%Y-%m-%d %H:%M:%S").timestamp())
    day1_time = current_time - 24 * 60 * 60
    end_time_local = time.localtime(day1_time)
    # start_time_local = time.localtime(day1_time + 60)
    # 昨天结束时间
    day1_end_data = time.strftime("%Y-%m-%d %H:%M:%S", end_time_local)
    # 昨天开始时间
    # day1_start_data = time.strftime("%Y-%m-%d %H:%M:%S", start_time_local)
    # 获取昨天数据
    yes_day1_df = get_price(
        security=assets_id,
        end_date=day1_end_data,
        count=1,
        frequency='daily', )
    # 返回昨日此刻的价格
    return yes_day1_df['close'].values[0]


# 获取所有A股最新价格
def a_last_all_price_func():
    # client = Client(token=UQ_TOKEN2)
    auth('18846444159', 'aA1192338674')
    # 组织查询时间
    end_t = time.time()
    start_t = time.time() - 60
    end_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_t))
    start_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_t))

    print(f'开始时间:{start_date} - 结束时间:{end_date} 所有A股实时价格')

    # 存放查到的所有A股实时的价格和时间存放格式： dict:{'code':{'money': ***, 'data': ****, ....}}
    price_dict = {}
    # 存放所有未找到的A股
    not_astocks_list = []

    with open('resource/xtech_astocks_sum.csv', 'r', encoding='utf8') as csvfile:
        csv_reader = csv.reader(csvfile)
        birth_header = next(csv_reader)
        for row in csv_reader:
            assets_id = row[1]
            assets_name = row[2]
            # market_type = row[0]
            try:
                df = get_price(
                    security=assets_id,
                    start_date=start_date,
                    end_date=end_date,
                    frequency='minute',)
                    # fields=['money'],
            except Exception as err:
                print(err)
                not_astocks_list.append(assets_id)
                continue
            # 临时列表，用于存放一个股票代码ID查到的所有数据
            row_list = []
            for index, row in df.iterrows():
                row_list.append({
                    'time': row.name.__str__(),
                    'datetime': row.name.__str__().split(' ')[0],
                    'assets_id': assets_id,
                    'assets_name': assets_name,
                    'sell_id': 'CNY',
                    'open_price': row.open,
                    'high_price': row.high,
                    'low_price': row.low,
                    'close_price': row.close,
                    'volume': row.volume,
                    'values': row.money,
                })
            # 取出最新的数据存放到最后返回的字典中
            try:
                # 制作hash_id并放入字典中
                # current_time = int(datetime.datetime.strptime(str(row_list[-1]['datetime']), "%Y-%m-%d").timestamp()) + 82800
                # hash_id = hash_sha3_256_bar(code, current_time)
                # row_list[-1]['hash_id'] = hash_id
                # 增加字段，涨跌幅
                # 获取昨天这个时间的价钱
                day1_close_price = get_yesterday_meanwhile_data(assets_id, row_list[-1]['time'])
                print(f"{assets_id}{assets_name}今天的close_price:{row_list[-1]['close_price']},昨天的close_price{day1_close_price},\涨幅是{row_list[-1]['close_price'] / day1_close_price - 1}")
                day1_change = row_list[-1]['close_price'] / day1_close_price - 1
                row_list[-1]['day1_change'] = day1_change
                # 整条信息存储到字典中
                price_dict[assets_id] = row_list[-1]
            except IndexError:
                print('A股%s无更新' %(assets_id))

    return price_dict


# 插入数据到测试库
def insert_a_last_all_price(price_dict):

    conn = psycopg2.connect(
        database=REMOTE_DATABASE,
        user=REMOTE_USER,
        password=REMOTE_PASSWORD,
        host=REMOTE_HOST,
        # port=REMOTE_PORT
    )
    # time = int(datetime.datetime.strptime(str(price_dict['time']), '%Y-%m-%d %H:%M:%S').timestamp())
    cursor = conn.cursor()
    sql = "insert into price_test (datetime, hash_id, assets_id, assets_name, sell_id, " \
                        "open_price, high_price, low_price, close_price, volume, value) \
                           VALUES (%s, '%s', '%s', '%s','%s', %s, %s, %s, %s, %s, %s)" % \
           ('2020-10-23\ 15\:00\:00',#str(price_dict['time'])
            price_dict['hash_id'],
            price_dict['assets_id'],
            price_dict['assets_name'],
            price_dict['sell_id'],
            price_dict['open_price'],
            price_dict['high_price'],
            price_dict['low_price'],
            price_dict['close_price'],
            price_dict['volume'],
            price_dict['values'])
    print(sql)
    cursor.execute(sql)
    print("insert crypto daily Kline successfully", 'price_test', price_dict['assets_id'], price_dict['assets_name'])

    # 事物提交
    conn.commit()
    # 关闭数据库连接
    conn.close()


if __name__ == '__main__':
    all_price = a_last_all_price_func()
    print(all_price)
    # td = '2020-10-26 11:22:30'
    # see_id = '000036.XSHE'
    # close_price = get_yesterday_meanwhile_data(see_id, td)
    # print(close_price)
