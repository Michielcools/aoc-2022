def main():
    file = open("input.txt", "r")
    input = file.readlines()
    i = 0
    totaal = 0
    while i < len(input):
        input[i] = input[i].strip("\n")
        i += 1
    i = 1
    j = 1
    while i < len(input)-1:
        while j < len(input[0])-1:
            totaal += check(input,i,j)
            j += 1
        i += 1
        j = 1
    totaal += (len(input)-1)*4
    print(totaal)

def check(input,i,j):
    getal = int(input[i][j])
    visible = True
    hz = j -1
    while hz >= 0:
        if int(input[i][hz]) >= getal:
            visible = False
            break
        hz -= 1
    if visible:
        return 1
    hz = j+1
    visible = True
    while hz < len(input[0]):
        if int(input[i][hz]) >= getal:
            visible = False
            break
        hz += 1
    if visible:
        return 1
    visible = True
    vt = i - 1
    while vt >= 0:
        if int(input[vt][j]) >= getal:
            visible = False
            break
        vt -= 1
    if visible:
        return 1
    visible = True
    vt = i + 1
    while vt < len(input):
        if int(input[vt][j]) >= getal:
            visible = False
            break
        vt += 1
    if visible:
        return 1
    return 0



        

main()