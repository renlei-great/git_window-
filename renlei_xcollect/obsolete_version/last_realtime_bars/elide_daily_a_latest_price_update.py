import csv
import time
import datetime

from jqdatasdk import *
import psycopg2

from local_settings import *


# client = Client(token=UQ_TOKEN2)
from utils.auto.autoupdate import auto_update

auth('18846444159', 'aA1192338674')


# CONN = psycopg2.connect(
#                     database=REMOTE_DATABASE,
#                     user=REMOTE_USER,
#                     password=REMOTE_PASSWORD,
#                     host=REMOTE_HOST,
#                     port=REMOTE_PORT
#                 )


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


# 出现空值后查询前天的价格，回滚最大十天查询价格循环
def a_day1_roll_back1(assets_id):

    for i in range(1, 11):
        # 组织查询时间
        end_t = time.time() - 60 * 60 * 24 * i
        end_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_t))

        df = get_price(
            security=assets_id,
            end_date=end_date,
            count=1,
            frequency='minute', )

        if not any([str(df['close'].values[0]) == 'nan', str(df['open'].values[0]) == 'nan',
                str(df['high'].values[0]) == 'nan',str(df['low'].values[0]) == 'nan',
                str(df['volume'].values[0]) == 'nan', ]):
            return df
    return False


# 获取所有A股最新价格
def a_last_all_price_func(exce_type='update'):
    # 组织查询时间
    end_t = time.time()
    end_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_t))

    print(f'时间:{end_date} 最新价格所有A股实时价格')

    # 建立数据库连接
    conn = psycopg2.connect(
        database=REMOTE_DATABASE,
        user=REMOTE_USER,
        password=REMOTE_PASSWORD,
        host=REMOTE_HOST,
        port=REMOTE_PORT
    )

    # 存放查到的所有A股实时的价格和时间存放格式： dict:{'code':{'money': ***, 'data': ****, ....}}
    # price_dict = {}
    # 存放所有未找到的A股
    not_astocks_list = []
    with open(RESOURCE_PATH + '\\xtech_astocks_sum1.csv', 'r', encoding='utf8') as csvfile:
        csv_reader = csv.reader(csvfile)
        birth_header = next(csv_reader)
        for row in csv_reader:
            assets_id = row[1]
            assets_name = row[2]
            # market_type = row[0]
            try:
                df = get_price(
                    security=assets_id,
                    end_date=end_date,
                    count=1,
                    frequency='minute',)
            except Exception as err:
                print(err)
                not_astocks_list.append(assets_id)
                continue

            # 判断查询的代码是否有空值
            if any([str(df['close'].values[0]) == 'nan', str(df['open'].values[0]) == 'nan',
                    str(df['high'].values[0]) == 'nan',str(df['low'].values[0]) == 'nan',
                    str(df['volume'].values[0]) == 'nan', ]):
                # 有控制调用下面函数进行回滚天数查询
                df = a_day1_roll_back1(assets_id)
                if not df:
                    print(f'{assets_id,assets_name}十天内数据均为空，不添加')
                    continue

            if exce_type == 'insert':
                # 将查询到的结果插到字典中,调用insert数据库的函数
                for index, row in df.iterrows():
                    price_dict = {
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
                        'value': row.money,
                    }

                # 增加字段，涨跌幅
                # 获取昨天这个时间的价钱
                day1_close_price = get_yesterday_meanwhile_data(assets_id, price_dict['time'])
                day1_change = price_dict['close_price'] / day1_close_price - 1
                price_dict['day1_change'] = day1_change

                # conn = psycopg2.connect(
                #     database=REMOTE_DATABASE,
                #     user=REMOTE_USER,
                #     password=REMOTE_PASSWORD,
                #     host=REMOTE_HOST,
                #     port=REMOTE_PORT
                # )

                # 插入数据到数据库中
                insert_a_last_all_price(conn, price_dict)
                # print(f'insert {assets_id}{assets_name}最新信息 ---> 数据库')

            else:
                # 将查询到的结果插到字典中,调用update数据库的函数
                for index, row in df.iterrows():
                    price_dict = {
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
                        'value': row.money,
                    }

                # 增加字段，涨跌幅
                # 获取昨天这个时间的价钱
                day1_close_price = get_yesterday_meanwhile_data(assets_id, price_dict['time'])
                day1_change = price_dict['close_price'] / day1_close_price - 1
                price_dict['day1_change'] = day1_change

                # conn = psycopg2.connect(
                #     database=REMOTE_DATABASE,
                #     user=REMOTE_USER,
                #     password=REMOTE_PASSWORD,
                #     host=REMOTE_HOST,
                #     port=REMOTE_PORT
                # )

                # 更新数据到数据库
                update_a_last_all_price(conn, price_dict)

                # print(f'update {assets_id}{assets_name}最新信息 ---> 数据库')

    conn.close()
    auto_update(a_last_all_price_func, hour=1)


# 插入数据到测试库
def insert_a_last_all_price(conn, price_dict):

    # conn = psycopg2.connect(
    #     database=REMOTE_DATABASE,
    #     user=REMOTE_USER,
    #     password=REMOTE_PASSWORD,
    #     host=REMOTE_HOST,
    #     port=REMOTE_PORT
    # )

    current_trade_timestamp = int(datetime.datetime.strptime(str(price_dict['datetime']), '%Y-%m-%d').timestamp()) + 82800
    cursor = conn.cursor()
    sql = "insert into %s (datetime, assets_id, assets_name, sell_id, " \
          "open_price, high_price, low_price, close_price, volume, value, day1_change) " \
          " VALUES (%s, '%s', '%s', '%s','%s', %s, %s, %s, %s, %s, %s)" % \
           (REMOTE_TABLE,
            current_trade_timestamp,
            price_dict['assets_id'],
            price_dict['assets_name'],
            price_dict['sell_id'],
            price_dict['open_price'],
            price_dict['high_price'],
            price_dict['low_price'],
            price_dict['close_price'],
            price_dict['volume'],
            price_dict['value'],
            price_dict['day1_change'])
    # print(sql)
    # cursor.execute(sql)
    # a = 1
    try:
        cursor.execute(sql)
    except psycopg2.Error as e:
        if e.pgcode == '23505':
            print(f'此记录已存在跳转到update更新记录')
            # conn.close()
            conn.commit()
            update_a_last_all_price(conn, price_dict)
    else:
        print("insert A share data successfully", 'price_test', price_dict['assets_id'], price_dict['assets_name'])

        # 事物提交
        conn.commit()
        # 关闭数据库连接
        # conn.close()


# 更新数据到测试库
def update_a_last_all_price(conn, price_dict):

    # conn = psycopg2.connect(
    #     database=REMOTE_DATABASE,
    #     user=REMOTE_USER,
    #     password=REMOTE_PASSWORD,
    #     host=REMOTE_HOST,
    #     port=REMOTE_PORT
    # )

    current_trade_timestamp = int(datetime.datetime.strptime(str(price_dict['datetime']), '%Y-%m-%d').timestamp()) + 82800
    cursor = conn.cursor()

    sql = "UPDATE %s SET sell_id='CNY', datetime=%s, assets_name='%s'," \
          "open_price=%s, high_price=%s, low_price=%s, close_price=%s, volume=%s, value=%s, day1_change=%s \
             WHERE assets_id='%s'" % \
          (REMOTE_TABLE,
           current_trade_timestamp,
           price_dict['assets_name'],
           price_dict['open_price'],
           price_dict['high_price'],
           price_dict['low_price'],
           price_dict['close_price'],
           price_dict['volume'],
           price_dict['value'],
           price_dict['day1_change'],
           price_dict['assets_id'],)

    cursor.execute(sql)

    if cursor.rowcount == 0:
        print("没有此数据更新失败跳转到insert插入数据")
        # conn.close()
        insert_a_last_all_price(conn, price_dict)
    else:
        print("Update A share data successfully", 'realtime_bars', price_dict['assets_id'], price_dict['assets_name'])

        # 事物提交
        conn.commit()
        # 关闭数据库连接
        # conn.close()


def run():
    start = datetime.datetime.now()
    a_last_all_price_func('update')
    end = datetime.datetime.now()
    print(end - start)


if __name__ == '__main__':
    run()
