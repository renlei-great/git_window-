import random,string


def random_str(type, number):
    ret = ''.join(random.sample(string.ascii_letters + string.digits if type == 'str+int' else
                                string.ascii_letters if type == 'str' else
                                string.digits if type == 'int' else
                                string.ascii_letters + string.digits, number))
    return ret
    # ''.join(random.sample(string.digits, number)) if type == 'int' else '类型错误'
    # ''.join(random.sample(string.ascii_letters, number)) if type == 'str' else '类型错误'


if __name__ == "__main__":
    print(random_str('int', 5))
    print(random_str('str', 6))
    print(random_str('str+int', 7))
    print(random_str('sss', 8))