import threading

from utils.auto.autoupdate import auto_update
from utils.last_realtime_bars.daily_a_latest_price_update import a_last_all_price_func
from utils.self_select_stock.users_add_optional_data import run


def auto_run(param_dict):  # appoint_key, appoint_hour
    threading.Thread(
        target=auto_update,
        kwargs={key: val for key, val in param_dict.items()}).start()


if __name__ == "__main__":

    # 自动执行
    # 存放要执行的模块以及参数
    ex_funcs = [{'func': run, 'minute': 5}, {'func': a_last_all_price_func, 'hour': 1}]

    # 遍历每个执行的模块
    for ex_func in ex_funcs:
        auto_run(ex_func)
