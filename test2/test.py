#
# a = None
#
# for i in a:
#     print(i)
import re


a = ",".join(re.findall('\w+', "[['z'], ['x']]")).replace(',','')
print(a)