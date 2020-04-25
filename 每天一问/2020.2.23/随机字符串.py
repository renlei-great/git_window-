import random, string

def genrendomstring():
    str_asc = string.ascii_letters
    print("as:" + str_asc)

    str_di = string.digits
    print("di:" + str_di)

    # return ''.join(random.sample(string.ascii_letters + string.digits, 5))
    return random.sample(string.ascii_letters + string.digits, 20)

print(genrendomstring())
print(genrendomstring())
print(genrendomstring())