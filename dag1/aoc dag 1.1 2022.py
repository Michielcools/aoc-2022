file = open("dag1.1test.txt", "r")
current = 0
max = 0
for line in file.readlines():
    if line != "\n":
        current += int(line)
    else:
        if current > max:
            max = current
        current = 0
print(max)

