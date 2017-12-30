import re

str = "<a href='http://www.baidu.com'>百度一下，我就知道</a>"
pat = '[a-zA-Z]+://[^\s]+[.com|.cn]'
rst = re.compile(pat).findall(str)
print(rst)
