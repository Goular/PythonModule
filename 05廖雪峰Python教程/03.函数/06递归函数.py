def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(1))
print(fact(10))
print(fact(100))
print(fact(1000)) # 数目太大，报错
