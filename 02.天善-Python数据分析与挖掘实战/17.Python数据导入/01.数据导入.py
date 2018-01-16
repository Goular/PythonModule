import pandas as pda

# 数据导入
# csv
# csv = pda.read_csv('./hexun.csv')
# print(csv.describe())
# print(csv.sort_values(by='21')) # 按照指定列进行排列

# 导入Excel数据
# excel = pda.read_excel('./abc.xls')
# print(excel.describe())

# 导入MySQL数据
# import pymysql
#
# conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='dangdang')
# sql = 'select * from goods'
# data = pda.read_sql(sql,conn)
# print(data.describe())

# 导入HTML数据
# html = pda.read_html('./abc.html')
# print(html)

# 导入在在线网页
# html = pda.read_html('https://book.douban.com')
# print(html)

# 导入文本
# text = pda.read_table('./abc.txt')
# print(text)
