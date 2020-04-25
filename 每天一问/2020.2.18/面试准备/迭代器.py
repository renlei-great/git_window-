
class DedaiQi():
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self.__next__()

    def __next__(self):
        self.i += 1
        return self.i

def main():
    dedai = DedaiQi()
    print(dedai.__iter__())
    print(dedai.__iter__())
    print(dedai.__iter__())


if __name__ == "__main__":
    main()