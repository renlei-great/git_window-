class Prose():
    cl = 3


class student(Prose):
    def __init__(self, name):
        self.name = name


def main():
    # pro = Prose()
    stu = student("renlei")
    stu.__dict__['name2'] = "haode"
    # print()
    print(stu.__dict__)


if __name__ == "__main__":
    main()