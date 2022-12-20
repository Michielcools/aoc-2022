def main():
    file = open("input.txt", "r")
    input = file.readlines()
    i = 0
    max = 0
    while i < len(input):
        input[i] = input[i].strip("\n")
        i += 1
    i = 1
    j = 1
    while i < len(input) - 1:
        while j < len(input[0]) - 1:
            getal = check(input, i, j)
            if getal > max:
                max = getal
            j += 1
        i += 1
        j = 1
    print(max)


def check(input, i, j):
    getal = int(input[i][j])
    hz = j - 1
    totaal = 1
    temp = 0
    while hz >= 0:
        temp += 1
        if int(input[i][hz]) >= getal:
            break
        hz -= 1
    totaal *= temp
    temp = 0
    hz = j + 1
    while hz < len(input[0]):
        temp += 1
        if int(input[i][hz]) >= getal:
            break
        hz += 1
    totaal *= temp
    temp = 0
    vt = i - 1
    while vt >= 0:
        temp += 1
        if int(input[vt][j]) >= getal:
            break
        vt -= 1
    totaal *= temp
    temp = 0
    vt = i + 1
    while vt < len(input):
        temp += 1
        if int(input[vt][j]) >= getal:
            break
        vt += 1
    totaal *= temp
    return totaal


main()