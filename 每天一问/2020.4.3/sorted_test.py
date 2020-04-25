alist = [{'name':'a','a':{'age': 20}},{'name':'b', 'a':{'age':30}},{'name':'c','a':{'age':25}}]

i = 0

def foo(x):
    # global i
    # x['cla'] = i
    # i +=1

    # return -x['a'].get('age')
    return (x >= 3, -x)

a = [1,2,3,9,0,5,-4,-2,-1,-6]
a = sorted(a, key=foo, reverse=True)  # lambda x: ((x>0),x))
print(a)