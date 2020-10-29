import datetime

import psycopg2

from local_settings import *
from utils.auto.autoupdate import auto_update


# 查询用户表中的每一个用户数据
def select_users_all():

    # 连接数据库
    conn = psycopg2.connect(
        database=REMOTE_DATABASE,
        user=REMOTE_USER,
        password=REMOTE_PASSWORD,
        host=REMOTE_HOST,
        port=REMOTE_PORT
    )
    cursor = conn.cursor()

    # 获取users表中所有数据
    # [(11, 1, 'cheney12345', 'wyqxiaoxyz@gmail.com', 0.0, ['600809.XSHG|山西汾酒|2020-10-27 08:32:09|207.53|0.019803439803439904']), (12, 1, '阿呆', '441161127@qq.com', 0.0, [])]
    sql = "select * from users"
    cursor.execute(sql)
    results_users = cursor.fetchall()

    # 关闭数据库连接
    conn.close()

    # 处理数据
    # 遍历每一个用户数据
    for user in results_users:
        processing_users_data(user)

    auto_update(select_users_all, minute=5)


# 将用户新的optional更新到users表中
def update_users_optional(user_id, update_optional_list):

    # 链接数据库
    conn = psycopg2.connect(
        database=REMOTE_DATABASE,
        user=REMOTE_USER,
        password=REMOTE_PASSWORD,
        host=REMOTE_HOST,
        port=REMOTE_PORT
    )
    cursor = conn.cursor()

    sql = "UPDATE users SET user_optional=%s WHERE id=%s"
    cursor.execute(sql, (update_optional_list, user_id))

    # 提交关闭数据库
    conn.commit()
    conn.close()


# 对取到的用户数据进行处理编辑
def processing_users_data(user):

    if not user[-1]:
        return

    # 链接数据库
    conn = psycopg2.connect(
        database=REMOTE_DATABASE,
        user=REMOTE_USER,
        password=REMOTE_PASSWORD,
        host=REMOTE_HOST,
        port=REMOTE_PORT
    )
    cursor = conn.cursor()

    # 修改后存放optional的列表
    update_optional_list = []

    # 遍历每个用户每一条optional记录，做出修改
    print(f'用户{user[2]}关注的股票:')
    for optional in user[-1]:
        user_optional = optional.split('|')
        assets_id = user_optional[0]
        old_price = user_optional[3]

        # 获取这只股票的最新数据
        sql = "select * from realtime_bars where assets_id='%s'" %(assets_id)
        cursor.execute(sql)
        results_realtime = cursor.fetchone()

        # assets_id | datetime | assets_name | sell_id | open_price | high_price | low_price | close_price | volume | value | day1_change
        print('股票信息：', results_realtime)

        # 现在的价格
        current_price = results_realtime[7]
        # 现在的涨跌幅
        current_price_limit = results_realtime[-1]
        # 入选到现在的涨跌幅
        old_current_price_limit = float(current_price) / float(old_price) - 1
        # 组织新的optional数据
        optional = "%s|%s|%s|%s|%s|%s|%s" % (user_optional[0], user_optional[1],
                                             user_optional[2], user_optional[3],
                                             current_price_limit, current_price,
                                             old_current_price_limit)

        # 把当前这一条自选股放入到列表中
        update_optional_list.append(optional)

    # 关闭数据库
    conn.close()
    print(f'把{update_optional_list}这条信息更新到users-->user_optional字段之前')
    # 更新users表的optional字段
    update_users_optional(user[0], update_optional_list)


def run():
    '''修改用户users表中的user_optional字段,添加实时信息'''
    select_users_all()



if __name__ == "__main__":
    run()
