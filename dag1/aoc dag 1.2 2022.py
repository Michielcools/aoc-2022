file = open("dag1.1test.txt", "r")
current = 0
max1 = 0
max2 = 0
max3 = 0
for line in file.readlines():
    if line != "\n":
        current += int(line)
    else:
        if current > max1:
            max3 = max2
            max2 = max1
            max1 = current
        elif current > max2:
            max3 = max2
            max2 = current
        elif current > max1:
            max3 = current
        current = 0
print(max1+max2+max3)

