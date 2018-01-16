import pandas as pda

# pandas库的使用
a = pda.Series([8, 9, 4, 5, 8, 9])
print(a)
b = pda.Series([8, 9, 4, 5, 8, 9], index=['one', 'two', 'three', 'four', 'five', 'six'])
print(b)

c = pda.DataFrame([[5, 6, 2, 3], [8, 4, 6, 3], [4, 6, 31, 9]])
print(c)

d = pda.DataFrame([[5, 6, 2, 3], [8, 4, 6, 3], [4, 6, 31, 9]], index=['aa', 'bb', 'cc'],
                  columns=['one', 'two', 'three', 'four'])
print(d)

e = pda.DataFrame({
    'one': 4,
    'two': [6, 5, 8, 5],
    'three': list(str(9823))
}, index=['a','b','c','d'])
print(e)

# 转置
print(e.T)

# 数据分析
print(d.describe())