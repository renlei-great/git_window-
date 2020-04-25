import re

strr = 'rest'
s = re.search(r'r.*', strr)
ss = re.search(r'r.*?', strr)
print(s)
print(ss)