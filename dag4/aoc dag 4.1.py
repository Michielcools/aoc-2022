import re
def main():
    file = open("input.txt", "r")
    totaaldubbels = 0
    for line in file:
        line = line.strip("\n")
        getallen = re.split(",|-",line)
        if (int(getallen[0]) <= int(getallen[2]) and int(getallen[1]) >= int(getallen[3])) or int(getallen[0])>= int(getallen[2]) and int(getallen[1]) <= int(getallen[3]):
            totaaldubbels += 1
    print(totaaldubbels)


main()