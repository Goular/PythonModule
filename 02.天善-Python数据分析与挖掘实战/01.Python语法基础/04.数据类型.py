# # 数字
# a = 1
# b = 1.1
# c = 1 + 6j
# print(a)
# print(b)
# print(c)
#
# # 字符串
# str = "Hello Python"
# print(str)
#
# # 列表
# abc_list = ['My', 'You', 'He']
# print(abc_list)
# print(abc_list[0])
# print(abc_list[1])
# print(abc_list[2])
#
# abc_list[1] = "GuangZhou"
# print(abc_list)
#
# # 元组 touble
# def_touple = ('I', 'Am', 'Python', 'Learn')
# print(def_touple)
# # def_touple[0] = 'Hello'
#
# # 集合set
# a = "kldjflkdsjlfsdf"
# b = "klfjlsoioiowelnlljk"
# # 字符串添加到集合会变为字符集合，会被拆分出来，所以添加一个列表会比较合适
# # sa = set(a)
# # sb = set(b)
# # print(sa)
# # print(sb)
# # print(sa & sb)  # 交集
# # print(sa | sb)  # 并集
# # print(sa - sb)  # 差集
#
# # 字典 即Java的HashMap的使用
# # abc_map = {'name': 'Goular', 'sex': 'male', 'age': 16}
# # print(abc_map)
# # print(abc_map['name'])
# # print(abc_map['sex'])
# # print(abc_map['age'])
# # abc_map['name'] = 'XiLa'
# # abc_map['age'] = 62
# # print(abc_map)
# # print(abc_map['name'])
# # print(abc_map['sex'])
# # print(abc_map['age'])

# 列表分片
list_abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
data = list_abc[:]
print(data)
data1 = list_abc[2:]
print(data1)
