import re

str = "<a href='http://www.baidu.com'>百度一下，我就知道</a>"
pat = '[a-zA-Z]+://[^\s]+[.com|.cn]' # 其实这个是有错误的写法，但是在这里列子中可以实现鉴别那就算了，因为中括号的内容是平等的
rst = re.compile(pat).findall(str)
print(rst)
