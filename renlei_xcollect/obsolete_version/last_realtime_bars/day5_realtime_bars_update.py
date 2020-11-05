import csv
import time
import datetime

from uqer import Client, DataAPI
from jqdatasdk import *
import psycopg2

from local_settings import *

# client = Client(token=UQ_TOKEN2)
from utils.auto.autoupdate import auto_update

auth('18846444159', 'aA1192338674')


# A股存放五天数据--->出现N条空值后查询前N条的价格，回滚最大30天查询价格循环，递归
def jk_a_day1_roll_back(assets_id, assets_name, temporary_list:list, num, end_date):

    # 记录错误条数
    record_null_num = 0
    # 判断是否出现五天的数据全部是空
    if not temporary_list:
        try:
            end_d = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')
        except TypeError:
            end_d = end_date
        num = 5
        end_date = end_d + datetime.timedelta(days=-5)
    else:
        end_date = datetime.datetime.strptime(temporary_list[0]['time'], '%Y-%m-%d %H:%M:%S') + datetime.timedelta(days=-1)

    day1_end_date = end_date.strftime('%Y-%m-%d %H:%M:%S')
    # 最大能回滚的时间
    year1_datetime = datetime.datetime.now() + datetime.timedelta(days=-30)

    if year1_datetime > end_date:
        return False

    df = get_price(
        security=assets_id,
        end_date=day1_end_date,
        count=num,
        frequency='daily', )


    # 将查询到的结果放到列表中
    for index, row in df.iterrows():

        # 判断查询的数据是否有空值
        if any([str(row['close']) in ['nan', 'NaN'],
                str(row['volume']) in ['nan', 'NaN'],
                str(row['money']) in ['nan', 'NaN'], ]):
            record_null_num += 1
            continue

        price_dict = {
            'time': row.name.__str__(),
            'datetime': row.name.__str__().split(' ')[0],
            'assets_id': assets_id,
            'assets_name': assets_name,
            'sell_id': 'CNY',
            'open_price': row.open if not row.open in ['nan', 'NaN'] else row.close,
            'high_price': row.high if not row.high in ['nan', 'NaN'] else row.high,
            'low_price': row.low if not row.low in ['nan', 'NaN'] else row.low,
            'close_price': row.close,
            'volume': row.volume,
            'value': row.money,
        }

        # 添加到临时列表中
        temporary_list.insert(0, price_dict)

    # 判断是否需要继续回滚
    if record_null_num != 0:
        jk_a_day1_roll_back(assets_id, assets_name, temporary_list, record_null_num, end_date)
    else:
        return True


# A股存放五天数据---> 从聚宽中查询csv文件中的所有股票IDd的行情信息，并将信息存放到数据库中
def jk_a_query_stock_quotation(conn, local_csv_name, end_date, exce_type='update'):
    with open(RESOURCE_PATH + '\\' + local_csv_name, 'r', encoding='utf8') as csvfile:
        csv_reader = csv.reader(csvfile)
        birth_header = next(csv_reader)
        for row in csv_reader:
            assets_id = row[1]
            assets_name = row[2]
            try:
                df = get_price(
                    security=assets_id,
                    end_date=end_date,
                    count=5,
                    frequency='daily', )
            except Exception as err:
                print('出错：',err)
                continue

            # 获取此股票在数据库中的信息,判断该执行的逻辑
            select_sql = "select * from day5_realtime_bars where assets_id='%s' order by datetime" % (assets_id)
            cursor = conn.cursor()
            cursor.execute(select_sql)
            print(cursor)

            # 执行插入逻辑
            if exce_type == 'insert':
                # 临时列表
                temporary_list = []
                # 记录有几条空值
                record_null_num = 0
                # 将查询到的结果插到字典中,调用insert数据库的函数
                for index, row in df.iterrows():

                    # 判断查询的数据是否有空值
                    if any([str(row['close']) in ['nan', 'NaN'],
                            str(row['volume']) in ['nan', 'NaN'],
                            str(row['money']) in ['nan', 'NaN'], ]):
                        record_null_num += 1
                        continue

                    price_dict = {
                        'time': row.name.__str__(),
                        'datetime': row.name.__str__().split(' ')[0],
                        'assets_id': assets_id,
                        'assets_name': assets_name,
                        'sell_id': 'CNY',
                        'open_price': row.open if not row.open in ['nan', 'NaN'] else row.close,
                        'high_price': row.high if not row.high in ['nan', 'NaN'] else row.high,
                        'low_price': row.low if not row.low in ['nan', 'NaN'] else row.low,
                        'close_price': row.close,
                        'volume': row.volume,
                        'value': row.money,
                    }

                    # 添加到临时列表中
                    temporary_list.append(price_dict)

                # 查看是否有失败的记录,如果有那么进行再次获取
                if record_null_num != 0:
                    jk_a_day1_roll_back(
                        assets_id=assets_id,
                        assets_name=assets_name,
                        temporary_list=temporary_list,
                        num=record_null_num,
                        end_date=end_date,
                    )

                # 如果列表不为空插入数据到数据库中
                if len(temporary_list) > 0:
                    for price_dict in temporary_list:
                        insert_a_last_all_price(conn, price_dict, 'day5_realtime_bars')
                else:
                    print(f'{assets_id}-{assets_name}:近一个月的数据为空，跳过本只股票')
            # 执行更像逻辑
            else:
                # 将查询到的结果插到字典中,调用update数据库的函数
                # 临时列表
                temporary_list = []
                # 记录有几条空值
                record_null_num = 0
                # 将查询到的结果插到字典中,调用insert数据库的函数
                for index, row in df.iterrows():

                    # 判断查询的数据是否有空值
                    if any([str(row['close']) in ['nan', 'NaN'],
                            str(row['volume']) in ['nan', 'NaN'],
                            str(row['money']) in ['nan', 'NaN'], ]):
                        record_null_num += 1
                        continue

                    price_dict = {
                        'time': row.name.__str__(),
                        'datetime': row.name.__str__().split(' ')[0],
                        'assets_id': assets_id,
                        'assets_name': assets_name,
                        'sell_id': 'CNY',
                        'open_price': row.open if not row.open in ['nan', 'NaN'] else row.close,
                        'high_price': row.high if not row.high in ['nan', 'NaN'] else row.high,
                        'low_price': row.low if not row.low in ['nan', 'NaN'] else row.low,
                        'close_price': row.close,
                        'volume': row.volume,
                        'value': row.money,
                    }

                    # 添加到临时列表中
                    temporary_list.append(price_dict)

                # 查看是否有失败的记录,如果有那么进行再次获取
                if record_null_num != 0:
                    jk_a_day1_roll_back(
                        assets_id=assets_id,
                        assets_name=assets_name,
                        temporary_list=temporary_list,
                        num=record_null_num,
                        end_date=end_date,
                    )

                # 如果列表不为空插入数据到数据库中
                if len(temporary_list) > 0:
                    for price_dict in temporary_list:
                        update_a_last_all_price(conn, price_dict, 'day5_realtime_bars')


# 从聚宽获取数据更新所有A股五天的最新价格
def a_day5_all_price_func(exce_type='update'):
    # 组织查询时间
    end_t = datetime.datetime.now()
    end_date = end_t.strftime('%Y-%m-%d %H:%M:%S')

    print(f'时间:{end_date} 最新价格所有A股五天的最新信息')

    # 建立数据库连接
    conn = psycopg2.connect(
        database=REMOTE_DATABASE,
        user=REMOTE_USER,
        password=REMOTE_PASSWORD,
        host=REMOTE_HOST,
        port=REMOTE_PORT
    )

    # 将初始参数传入获取最新的五天信息，并插入到数据库中
    csv_names = ['xtech_astocks_sum1.csv', 'xtech_index_sum_brief.csv']
    for csv_name in csv_names:
        jk_a_query_stock_quotation(conn=conn,
                                   end_date=end_date,
                                   local_csv_name=csv_name,
                                   exce_type=exce_type,
                                   )

    conn.close()
    # auto_update(a_last_all_price_func, hour=1)


# 插入数据库
def insert_a_last_all_price(conn, price_dict, table_name):

    current_trade_timestamp = int(
        datetime.datetime.strptime(str(price_dict['datetime']), '%Y-%m-%d').timestamp()) + 82800
    cursor = conn.cursor()
    sql = "insert into %s (datetime, assets_id, assets_name, sell_id, " \
          "open_price, high_price, low_price, close_price, volume, value)" \
          " VALUES (%s, '%s', '%s', '%s','%s', %s, %s, %s, %s, %s)" % \
          (table_name,
           current_trade_timestamp,
           price_dict['assets_id'],
           price_dict['assets_name'],
           price_dict['sell_id'],
           price_dict['open_price'],
           price_dict['high_price'],
           price_dict['low_price'],
           price_dict['close_price'],
           price_dict['volume'],
           price_dict['value'],)
    print(sql)

    try:
        cursor.execute(sql)
    except psycopg2.Error as e:
        if e.pgcode == '23505':
            print(f'此记录已存在跳转到update更新记录')
            # conn.close()
            conn.commit()
            update_a_last_all_price(conn, price_dict, table_name)
        else:
            raise e
    else:
        print("insert A share data successfully", table_name, price_dict['assets_id'], price_dict['assets_name'])

        # 事物提交
        conn.commit()
        # conn.close()


# 更新数据到测试库
def update_a_last_all_price(conn, price_dict, table_name):

    current_trade_timestamp = int(
        datetime.datetime.strptime(str(price_dict['datetime']), '%Y-%m-%d').timestamp()) + 82800
    cursor = conn.cursor()

    sql = "UPDATE %s SET sell_id='CNY', datetime=%s, assets_name='%s'," \
          "open_price=%s, high_price=%s, low_price=%s, close_price=%s, volume=%s, value=%s WHERE assets_id='%s'" % \
          (table_name,
           current_trade_timestamp,
           price_dict['assets_name'],
           price_dict['open_price'],
           price_dict['high_price'],
           price_dict['low_price'],
           price_dict['close_price'],
           price_dict['volume'],
           price_dict['value'],
           price_dict['assets_id'],)
    # print(sql)
    cursor.execute(sql)

    if cursor.rowcount == 0:
        print("没有此数据更新失败跳转到insert插入数据")
        # conn.close()
        conn.commit()
        insert_a_last_all_price(conn, price_dict, table_name)
    else:
        print("Update A share data successfully", table_name, price_dict['assets_id'], price_dict['assets_name'])

        # 事物提交
        conn.commit()
        # conn.close()


def run():
    start = datetime.datetime.now()
    # a_last_all_price_func('update')
    # dfief_last_all_price_func('insert')
    a_day5_all_price_func('insert')
    end = datetime.datetime.now()
    print(end - start)


if __name__ == '__main__':
    run()
