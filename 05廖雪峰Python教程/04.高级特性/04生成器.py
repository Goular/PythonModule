# L = [x * x for x in range(10)]
# print(L)
# L = (x * x for x in range(10))
# print(L)
# print(next(L))
# print(next(L))
# print(next(L))
# print(next(L))
#
# print("---------------------------------")
#
# L2 = (x * x for x in range(20))
# for n in L2:
#     print(n)

# 斐波那契数列
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         # print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'


# print(fib(20))
# for value in fib(20):
#     print(value)

#  获取最后return的内容
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g', x)
#     except StopIteration as e: # 最后获取return的内容
#         print('Generator return value:', e.value)
#         break

    # def odd1():
    #     print('step 1')
    #     print('step 2')
    #     print('step 3')
    # odd1()

    # def odd():
    #     print('step 1')
    #     yield 1
    #     print('step 2')
    #     yield (3)
    #     print('step 3')
    #     yield (5)
    #
    #
    # o = odd()  # 第一步运行该方法会变为一个generator
    # print(odd)
    # print(o)
    # print("-------------------------------------------")
    # next(o)
    # next(o)
    # next(o)
