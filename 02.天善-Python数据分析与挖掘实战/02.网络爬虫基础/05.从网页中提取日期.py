from urllib.request import urlopen
import re

url = 'https://www.jianshu.com/p/42e11515c10f'
data = urlopen(url).read()

# <span class="publish-time" data-toggle="tooltip" data-placement="bottom" title="最后编辑于 2017.12.11 11:26">2016.08.05 11:21*</span>
pat = '<span class="publish-time"\s*data-toggle="tooltip"\s*data-placement="bottom"\s*title=".*?">(.*?)</span>'
rst = re.compile(pat).findall(str(data))
print(rst)