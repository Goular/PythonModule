# 由于re.match和re.search都是只会返回一个内容，re.match只会从头匹配
# 为了获取多个信息，我们需要采用re.compile().findall()
import re

pat = 'p.*?y'
string = 'pfklykkkkyklomp123ypoy'
rst = re.compile(pat).findall(string)
print(rst)
