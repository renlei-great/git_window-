import re
str1 = 'function'
str2 = 'func'

print(re.match('tion', str1))
print(re.search('tion', 'function'))
print(re.search('tion', str1))