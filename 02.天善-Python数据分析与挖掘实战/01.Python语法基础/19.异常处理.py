# 直接报错
# print("Hello")
# s6()

# 标准写法
# try:
#     print("Hello")
#     s6()
# except Exception as err:
#     print(err)

# 抛出异常
try:
    print("hello")
    raise Exception("sb")
except Exception as err:
    print(err)
