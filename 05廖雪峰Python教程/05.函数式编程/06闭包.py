def createCounter():
    def counter():
        return 1

    return counter


f1 = createCounter()
print(f1())
