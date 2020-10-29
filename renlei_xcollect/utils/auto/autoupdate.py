import datetime
import threading


# 定时自动更新-根据参数选择是天更新还是时更新或分更新
def auto_update(func, day=0, hour=0, minute=0, appoint_hour='00'):
    '''
    定时自动更新
    :param func: 执行的函数
    :param day: 几天执行一次，(day,hour,minute只可出现一个)
    :param hour: 几小时执行一次，(day,hour,minute只可出现一个)
    :param minute: 几分钟执行一次，(day,hour,minute只可出现一个)
    :param appoint_hour: 每天的那个时辰执行,(当day参数有东西时此参数起作用)
    :return:
    '''

    # 获取现在时间
    now_time = datetime.datetime.now()

    # 获取下个时间
    if day != 0:
        next_time = now_time + datetime.timedelta(days=day)
        next_hour = appoint_hour
        next_minute = '00'
    elif hour != 0:
        next_time = now_time + datetime.timedelta(hours=hour)
        next_hour = next_time.hour
        next_minute = '00'
    elif minute != 0:
        next_time = now_time + datetime.timedelta(minutes=minute)
        next_hour = next_time.hour
        next_minute = next_time.minute
    else:
        raise ValueError('请给day,hour,minute其中一个参数赋值，只可以赋值一个参数')

    next_year = next_time.date().year
    next_month = next_time.date().month
    next_day = next_time.date().day

    print(str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " " + str(next_hour) + ":" + str(next_minute) + ":00  执行：", func)
    # 拼接下次执行时间，得出时间戳
    next_time = datetime.datetime.strptime(str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " " + str(next_hour) + ":" + str(next_minute) + ":00",
                                           "%Y-%m-%d %H:%M:%S")

    # 获取距离下个整点时间，单位为秒
    timer_start_time = (next_time - now_time).total_seconds()
    print(timer_start_time)

    # 定时器, 参数为(多少时间后执行，单位为秒，执行的方法)
    timer = threading.Timer(timer_start_time, func)
    timer.start()


# 没写成功
# def auto_update_decorator(day=0, hour=0, minute=0, appoint_hour='00'):
#     def auto_up(func):
#         def wrapped(*args, **kwargs):
#             func(*args, **kwargs)
#             auto_update(
#                 func=func,
#                 day=day,
#                 hour=hour,
#                 minute=minute,
#                 appoint_hour=appoint_hour)
#         return wrapped
#     return auto_up


# @auto_update_decorator(minute=1)
def test():
    print('我是测试函数')
    auto_update(func=test, minute=1)


if __name__ == "__main__":
    # auto_update_hour(1, test)
    # auto_update_minute(3, test)
    # auto_update(day=1, appoint_hour='05', func=test)
    test()