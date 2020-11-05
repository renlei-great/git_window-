import csv
import time
import datetime
import hashlib

from uqer import Client, DataAPI
from jqdatasdk import *
import psycopg2

from local_settings import *

# client = Client(token=UQ_TOKEN2)
from utils.auto.autoupdate import auto_update

auth('18846444159', 'aA1192338674')


# 暂时用不到
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
        end_date = end_d + datetime.timedelta(days=-2)
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


# 暂时用不到
# 从聚宽获取天数据，自动组织数据，并进行过滤空值
def jk_get_a_organize_data(assets_id, assets_name, end_date, count):

    df = get_price(
        security=assets_id,
        end_date=end_date,
        count=count,
        frequency='daily', )

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

    return temporary_list


# 从聚宽获取前[一天]五分钟数据，自动组织数据，并进行过滤空值
def jk_get_minute_a_organize_data(assets_id, assets_name,start_date, end_date, count_day):
    # 存放所有记录
    price_all_list = []
    # 记录查询的是第几天
    day_num = 0
    # 记录回滚次数
    roll_back_num = 0
    on_off = True
    while on_off:
        df = get_price(
            security=assets_id,
            start_date=start_date,
            end_date=end_date,
            frequency='5m',
            skip_paused=True,
        )

        # 临时存放记录列表
        temporary_list = []
        # 将查询到的结果插到字典中,存放到列表中
        for index, row in df.iterrows():
            # 判断查询的数据是否有空值
            # if any([str(row['close']) in ['nan', 'NaN'],
            #         str(row['volume']) in ['nan', 'NaN'],
            #         str(row['money']) in ['nan', 'NaN'], ]):
            #     continue

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

        # 判断此次查询是否有效
        if len(temporary_list) > 0:
            # 将结果存放在列表中
            price_all_list.extend(temporary_list)
            day_num += 1

        # 判断是否查询够了天数
        if day_num == count_day:
            on_off = False

        # 判断是否超出最大回滚天数
        if roll_back_num > 30:
            on_off = False

        # 改变下次查询时间
        start_d = datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(days=-1)
        end_d = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(days=-1)
        start_date = start_d.strftime('%Y-%m-%d %H:%M:%S')
        end_date = end_d.strftime('%Y-%m-%d %H:%M:%S')

        roll_back_num += 1

    return price_all_list


# A股存放[一天]数据---> 从聚宽中查询csv文件中的所有股票IDd的行情信息，并将信息存放到数据库中
def jk_a_query_stock_quotation(conn, local_csv_name, day_date, table_name):
    with open(RESOURCE_PATH + '/' + local_csv_name, 'r', encoding='utf8') as csvfile:
        csv_reader = csv.reader(csvfile)
        birth_header = next(csv_reader)
        start_date = day_date + ' 9:30:00'
        end_date = day_date + ' 15:00:00'
        # 循环执行主要逻辑
        for row in csv_reader:
            assets_id = row[1]
            assets_name = row[2]

            # 获取此股票在数据库中的信息
            min_d = day_date + ' 00:00:00'
            max_d = day_date + ' 23:59:59'
            time.localtime()
            min_date = time.strptime(min_d, '%Y-%m-%d %H:%M:%S')
            min_date = time.mktime(min_date)
            max_date = time.strptime(max_d, '%Y-%m-%d %H:%M:%S')
            max_date = time.mktime(max_date)

            select_sql = "select * from minute_kline where assets_id='%s' and datetime > %s and datetime < %s   order by datetime" % (assets_id, min_date, max_date)
            cursor = conn.cursor()
            cursor.execute(select_sql)
            conn.commit()
            real_all = cursor.fetchall()

            # 判断数据库中是否存在最新此股票数据
            if len(real_all) > 0:
                # 如果此股票已有数据，判断此数据是新的还是旧的，如果是旧的删掉，新的跳过
                # 获取数据库中最新的数据的时间
                # db_new_datetime = time.strftime(
                #     '%Y-%m-%d %H:%M:%S',
                #     time.localtime(real_all[-1][2]))
                # if db_new_datetime.split(' ')[0] == end_date.split(' ')[0]:
                # 有最新的数据，时间推前一天，删掉之前的旧数据
                date_time = datetime.datetime.strptime(
                    end_date.split(' ')[0]+' 23:59:59',
                    '%Y-%m-%d %H:%M:%S'
                )
                date_time = date_time + datetime.timedelta(days=-1)
                date_time = date_time.timestamp()
                delete_a_time_quantum_date(conn, assets_id, assets_name, date_time, table_name)
                print(f"{assets_id}-{assets_name} 此股票已是最新数据")
                continue
            else:
                # 删掉此股票小于当前查询时间的所有数据
                date_time = datetime.datetime.strptime(
                    end_date.split(' ')[0] + ' 23:59:59',
                    '%Y-%m-%d %H:%M:%S'
                )
                date_time = date_time.timestamp()
                delete_a_time_quantum_date(conn, assets_id, assets_name, date_time, table_name)

            # 数据库中未有最新数据，或未有过此股票旧信息，进行插入操作
            try:
                temporary_list = jk_get_minute_a_organize_data(
                    assets_id=assets_id,
                    assets_name=assets_name,
                    start_date=start_date,
                    end_date=end_date,
                    count_day=1)
            except Exception as err:
                print('出错：', err)
                if '找不到标的' in str(err):
                    continue
                else:
                    raise err
            # 如果列表不为空插入数据到数据库中
            if len(temporary_list) > 0:
                for price_dict in temporary_list:
                    insert_a_last_all_price(conn, price_dict, table_name)
                print("insert A share data successfully", table_name, price_dict['assets_id'],
                      price_dict['assets_name'])

            else:
                print(f'{assets_id}-{assets_name}:近一个月的数据为空，跳过本只股票')


# 从聚宽获取数据更新所有A股最新的[一天]每五分钟的价格
def a_day2_all_price_main():
    # 组织查询最晚时间时间
    end_t = datetime.datetime.now() + datetime.timedelta(days=-1)
    # 判断时间是否为礼拜天时间
    if end_t.weekday() == 5:
        # 如果是周六，退回周五
        end_t = datetime.datetime.now() + datetime.timedelta(days=-1)
    elif end_t.weekday() == 6:
        # 如果是周日，退回周五
        end_t = datetime.datetime.now() + datetime.timedelta(days=-2)
    day_date = end_t.strftime('%Y-%m-%d')

    print(f'时间:{day_date} 最新价格所有A股五天的最新信息')

    # 操作数据库的名称
    table_name = 'minute_kline'

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
        jk_a_query_stock_quotation(
            conn=conn,
            day_date=day_date,
            local_csv_name=csv_name,
            table_name=table_name,
        )

    conn.close()

    auto_update(a_day2_all_price_main, day=1)


# A股[实时]数据更新核心逻辑
def jk_a_last_query_stock_quotation(conn, local_csv_name, start_date, end_date):
    with open(RESOURCE_PATH + '/' + local_csv_name, 'r', encoding='utf8') as csvfile:
        csv_reader = csv.reader(csvfile)
        birth_header = next(csv_reader)

        # 循环执行主要逻辑
        for row in csv_reader:
            assets_id = row[1]
            assets_name = row[2]
            try:
                df = get_price(
                    security=assets_id,
                    start_date=end_date,
                    end_date=end_date,
                    frequency='5m',
                    # count=1,
                    skip_paused=True,
                )
            except Exception as err:
                print('出错:', err)
                continue

            if df.size == 0:
                print(f'{assets_id}-{assets_name}:无更新')
                continue
            # 将查询到的结果插到字典中,存放到列表中
            for index, row in df.iterrows():
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

                insert_a_last_all_price(conn, price_dict, 'minute_kline')


# 从聚宽[实时]更新当天数据入口，基础数据组织
def a_last_all_price_main():
    # 组织查询时间
    end_t = datetime.datetime.now()
    start_t = datetime.datetime.now() + datetime.timedelta(minutes=-5)
    end_date = end_t.strftime('%Y-%m-%d %H:%M:%S')
    start_date = start_t.strftime('%Y-%m-%d %H:%M:%S')


    print(f'时间:{end_date}-{end_date} 最新价格所有A股五分钟内的最新信息')

    # 建立数据库连接
    conn = psycopg2.connect(
        database=REMOTE_DATABASE,
        user=REMOTE_USER,
        password=REMOTE_PASSWORD,
        host=REMOTE_HOST,
        port=REMOTE_PORT
    )

    # 将初始参数传入获取最新的五分钟信息，并插入到数据库中
    csv_names = ['xtech_astocks_sum1.csv', 'xtech_index_sum_brief.csv']
    for csv_name in csv_names:
        jk_a_last_query_stock_quotation(conn=conn,
                                        start_date=start_date,
                                        end_date=end_date,
                                        local_csv_name=csv_name,
                                        )

    conn.close()
    # 判断当前时间是否是9:00-11:30 13:00-15:00，是否是星期六日
    current_datetime = datetime.datetime.now()
    if current_datetime.weekday() in [5,6]:
        pass

    auto_update(a_last_all_price_main, minute=1)


# 删除数据库中的一个时间段内的数据
def delete_a_time_quantum_date(conn, assets_id, assets_name, date_time, table_name):

    sql = "delete from %s where assets_id='%s' and datetime <= %s" % (table_name, assets_id, date_time)

    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    date_t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(date_time))
    print(f"删除{assets_id}-{assets_name} {date_t}之前的所有数据成功")


# 生成hash_id
def hash_sha3_256_ef(assets_id, datetime, low_price, close_price, volume, value):
    x = hashlib.sha256()
    x.update(assets_id.encode())
    x.update(datetime.encode())
    x.update(low_price.encode())
    x.update(close_price.encode())
    x.update(volume.encode())
    x.update(value.encode())
    return x.hexdigest()


# 插入数据库
def insert_a_last_all_price(conn, price_dict, table_name):
    # 制作时间
    current_trade_timestamp = int(
        datetime.datetime.strptime(str(price_dict['time']), '%Y-%m-%d %H:%M:%S').timestamp())  # + 82800
    # 制作hash_id
    hash_id = hash_sha3_256_ef(
        price_dict['assets_id'],
        price_dict['assets_name'],
        price_dict['low_price'],
        price_dict['close_price'],
        price_dict['volume'],
        price_dict['value'],
    )
    cursor = conn.cursor()
    sql = "insert into %s (hash_id, datetime, assets_id, assets_name, sell_id, " \
          "open_price, high_price, low_price, close_price, volume, value)" \
          " VALUES (%s, %s, '%s', '%s', '%s','%s', %s, %s, %s, %s, %s)" % \
          (table_name,
           hash_id,
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
    # print(sql)

    try:
        cursor.execute(sql)
    except psycopg2.Error as e:
        if e.pgcode == '23505':
            print(f'此记录已存在跳转到update更新记录')
            # conn.close()
            conn.commit()
            # update_a_last_all_price(conn, price_dict, table_name)
        else:
            raise e
    else:
        pass
        # print("insert A share data successfully", table_name, price_dict['assets_id'], price_dict['assets_name'])

        # 事物提交
        conn.commit()
        # conn.close()


# 更新数据库
def update_a_last_all_price(conn, price_dict, table_name):

    current_trade_timestamp = int(
        datetime.datetime.strptime(str(price_dict['time']), '%Y-%m-%d %H:%M:%S').timestamp()) + 82800
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
    a_day2_all_price_main()
    # print(111)
    # a_last_all_price_main()
    end = datetime.datetime.now()
    print(end - start)


if __name__ == '__main__':
    run()
