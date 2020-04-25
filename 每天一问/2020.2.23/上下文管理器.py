
class aa():
    def __init__(self):
        self.a = 4

    def __enter__(self):
        print('enter')
        return 'enter返回'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')


with aa() as e:
    print(e)
