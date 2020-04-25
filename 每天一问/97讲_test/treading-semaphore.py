import time
import threading


class CaryyOutHtml(threading.Thread):
    def __init__(self, emp:threading.Semaphore):
        super().__init__()
        self.emp = emp

    def run(self):
        time.sleep(2)
        print('HTML To obtain complete')
        self.emp.release()


class CaptrueUrl(threading.Thread):
    def __init__(self, emp:threading.Semaphore):
        super().__init__()
        self.emp = emp

    def run(self) -> None:

        for i in range(20):
            self.emp.acquire()
            html_caryy = CaryyOutHtml(self.emp)
            html_caryy.start()


if __name__ == "__main__":
    emp = threading.Semaphore(3)

    capt = CaptrueUrl(emp)
    capt.start()