def main():
    file = open("input.txt", "r")
    totaalprioriteit = 0
    for line in file:
        for letter in line[0:int((len(line))/2)]:
            if letter in line[int((len(line))/2):len(line)]:
                commonletter = letter
        if commonletter.isupper():
            totaalprioriteit += ord(commonletter)-38
        else:
            totaalprioriteit += ord(commonletter)-96
    print(totaalprioriteit)

main()