import re
def main():
    file = open("input.txt", "r")
    totaaldubbels = 0
    for line in file:
        alreadyfound = False
        line = line.strip("\n")
        getallen = re.split(",|-",line)
        i = int(getallen[0])
        while i <= int(getallen[1]):
            if i >= int(getallen[2]) and i <= int(getallen[3]) and not alreadyfound:
                totaaldubbels += 1
                alreadyfound = True

            i+=1
    print(totaaldubbels)
main()