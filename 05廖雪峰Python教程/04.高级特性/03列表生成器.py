print(list(range(0, 11)))
print("------------------------------------------")
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
print("------------------------------------------")
print([x * x for x in range(1, 11)])
print("------------------------------------------")
print([x * x for x in range(1, 11) if x % 2 == 0])
print("------------------------------------------")
print([m + n + o for m in 'abc' for n in 'def' for o in 'xyz'])
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

print(isinstance('123',int))