# -*- coding: utf-8 -*-


import threading

from test_for.event_update import hourly_update
from utils.auto.autoupdate import auto_update
from utils.last_realtime_bars.day2_realtime_bars_update3 import a_last_all_price_main
from obsolete_version.last_realtime_bars.elide_daily_a_latest_price_update import a_last_all_price_func
from utils.self_select_stock.users_add_optional_data import run


def auto_exec(param_dict):  # appoint_key, appoint_hour
    threading.Thread(
        target=auto_update,
        kwargs={key: val for key, val in param_dict.items()}).start()


def run_exec():
    # 自动执行
    # 存放要执行的模块以及参数
    ex_funcs = [
        {'func': run, 'minute': 5},
        {'func': a_last_all_price_func, 'hour': 1},
        {'func': hourly_update, 'day': 1, 'appoint_hour': '03'}
    ]

    # 遍历每个执行的模块
    for ex_func in ex_funcs:
        auto_exec(ex_func)
# print(0)
# run_exec()
# print(1)
if __name__ == "__main__":

    # 自动执行
    # 存放要执行的模块以及参数
    ex_funcs = [
        # {'func': run, 'minute': 1},
        {'func': a_last_all_price_main, 'minute': 1}
    ]

    # 遍历每个执行的模块
    for ex_func in ex_funcs:
        auto_exec(ex_func)
