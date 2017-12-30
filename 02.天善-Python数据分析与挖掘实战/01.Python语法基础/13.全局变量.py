a = 12



def print_a():
    global b
    b = 18
    print('hello print_a')


print_a()
print(b)
