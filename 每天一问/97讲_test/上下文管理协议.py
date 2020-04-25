class GuanLi:

    def __enter__(self):
        print("我是执行前加的功能")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("我是执行后加的语句")

    def age(self):
        print("我是执行中的语句")


if __name__ == "__main__":
    # guanli = GuanLi()
    # guanli.age()
    with GuanLi() as e:
        e.age()


