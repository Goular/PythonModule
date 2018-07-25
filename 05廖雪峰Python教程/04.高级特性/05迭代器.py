from collections import Iterable
from collections import Iterator

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(20)), Iterable))
print(isinstance(200, Iterable))

print("---------------------------------------------")
print(isinstance(iter('abc'), Iterator))
