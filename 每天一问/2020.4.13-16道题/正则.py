import re
strr = 'python Locatino\env\Scripts\python.exe" "E:/python Locatino/每天一问/2020.4.13-16道题/深浅拷贝.py'

s = r'python|Locatino'


ret = re.sub(s, '蟒蛇', strr)
print(ret)

restr = strr.replace('python', '蟒蛇')
print(restr)