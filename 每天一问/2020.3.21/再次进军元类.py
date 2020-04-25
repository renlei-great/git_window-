class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        print('被调用')
        return super().__new__(cls, *args, **kwargs)


class User(metaclass=MetaClass):
    # def __new__(cls, *args, **kwargs):
    #     print('user','被调用')
    #     return super().__new__(cls)

    def __init__(self):
        self.name = 1

class User1(User):
    pass


# user = User()
# print(user.name)