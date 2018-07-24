def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


print(calc(1))
print(calc(1, 2))
print(calc(1, 2, 3))
