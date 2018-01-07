# 第一版
# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n += 1
# fab(5)

# 第二版
# def fab(max):
#     n, a, b = 0, 0, 1
#     L = []
#     while n < max:
#         L.append(b)
#         a, b = b, a + b
#         n += 1
#     return L
#
#
# L = fab(6)
# for index in range(0, len(L)):
#     print(L[index])

# 第三版
# class Fab(object):
#     def __init__(self, max):
#         self.max = max
#         self.n, self.a, self.b = 0, 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n < self.max:
#             r = self.b
#             self.a, self.b = self.b, self.a + self.b
#             self.n = self.n + 1
#             return r
#         raise StopIteration()
#
#
# for n in Fab(5):
#     print(n)

# 第四版 yield
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        yield b
        a, b = b, a + b
        n += 1

#
# for n in fab(5):
#     print(n)

f = fab(5)
f.__next__()
f.__next__()
f.__next__()
f.__next__()
f.__next__()
