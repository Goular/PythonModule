from urllib.request import urlopen
import re

url = 'https://read.douban.com/provider/all'
data = urlopen(url).read()

# <div class="name">北京师范大学出版社</div>
pat = '<div\s*class="name">(.*?)</div>'
rst = re.compile(pat).findall(str(data.decode('utf-8')))

fh = open("./save.txt", "w")

it = iter(rst)
for data in it:
    fh.writelines(str(len(data)) + "\n")
    print(str(data))
fh.close()
