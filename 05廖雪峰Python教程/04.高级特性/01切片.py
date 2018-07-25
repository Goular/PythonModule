l = []
for i in range(0, 9):
    l.append(i)
print(l)
print(l[2:3])


def trim(str):
    while str[:1] == ' ':
        str = str[1:]

    while str[-1:] == ' ':
        str = str[:-1]
    return str


str = "  123  123 159      "
print(trim(str))
