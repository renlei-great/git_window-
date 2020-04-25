import threading

class TianMao(threading.Thread):
    def __init__(self, name, cond:threading.Condition):
        super().__init__()
        self.name = name
        self.cond = cond


    def run(self):
        with self.cond:
            print('{}:小爱同学'.format(self.name))
            self.cond.notify()
            self.cond.wait()

            print('{}:小爱同学'.format(self.name))
            self.cond.notify()
            self.cond.wait()

            print('{}:小爱同学'.format(self.name))
            self.cond.notify()
            self.cond.wait()

class XiaoAi(threading.Thread):
    def __init__(self, name, cond:threading.Condition):
        super().__init__()
        self.name = name
        self.cond = cond


    def run(self):
        with self.cond:
            self.cond.wait()
            print('{}:我在'.format(self.name))
            self.cond.notify()

            self.cond.wait()
            print('{}:我在'.format(self.name))
            self.cond.notify()

            self.cond.wait()
            print('{}:我在'.format(self.name))
            self.cond.notify()



if __name__ == "__main__":

    cond = threading.Condition()

    tianmao = TianMao('天猫', cond)
    xiaoai = XiaoAi('小爱', cond)

    xiaoai.start()
    tianmao.start()
