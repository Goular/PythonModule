import re

# 普通字符
# pat = "yue"
# str = "http://yum.iqianyue.com"
# rst1 = re.search(pat, str)
# print(rst1)

# 返回结果为none
# str = 'abcssdds'
# pat = 'yue'
# rst2 = re.search(pat, str)
# print(rst2)

# pat = "\n"
# str = '''klksdjflkds
# jfkldsfkl
# '''
# data = re.search(pat, str)
# print(data)

# str = "hgsjlsdj7pythonjkldfls"
# pat = '\w\dpython\w'
# rst3 = re.search(pat, str)
# print(rst3)

# pat='pyth[jsz]n'
# # str = 'jsldkjfldspythonlfjds'
# str = 'jsldkjfldspythjnlfjds'
# data = re.search(pat,str)
# print(data)

# pat = 'php|python'
# str = "kldsjfphpjlsdfjkdspythondsgsdf"
# rst1 = re.search(pat,str)
# print(rst1)

# pat1 = 'python'
# pat2 = 'python'
# str = 'jdskfjPythonlksdjsdl'
# rst1 = re.search(pat1, str)
# print(rst1)
# # 使用了模式修正符
# rst2 = re.search(pat2, str, re.I)
# print(rst2)

# 贪婪模式与懒惰模式
pat1 = 'p.*y'  # 贪婪模式
pat2 = 'p.*?y'  # 懒惰模式
str = 'jdsfjldskpytondsfsdy'
rst1 = re.search(pat1,str)
rst2 = re.search(pat2,str)
print(rst1)
print(rst2)
