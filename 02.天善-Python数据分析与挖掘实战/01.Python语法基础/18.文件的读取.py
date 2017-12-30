fh = open("./file3.txt", "r")
while True:
    line = fh.readline()
    if len(line) == 0:
        break
    print(line)
fh.close()
