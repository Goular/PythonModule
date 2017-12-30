import re

# re.match的使用
pat1 = 'p.*y'
string = 'ythdjsdlfjsdklflsdfjpsdjfkyldsy' #找到匹配
string = 'ythdjsdlfjsdklflsdfjpsdjfkyldsy' #找不到匹配 none
rst1 = re.match(pat1, string)
print(rst1)

