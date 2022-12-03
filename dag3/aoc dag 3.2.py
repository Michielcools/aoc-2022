def main():
    file = open("input.txt", "r")
    i = 0
    lines = file.readlines()
    totaalprioriteit = 0
    while i < len(lines):
        for letter in lines[i][:-1]:
            if letter in lines[i+1] and letter in lines[i+2]:
                badge = letter
        i+= 3
        if badge.isupper():
            totaalprioriteit += ord(badge)-38
        else:
            totaalprioriteit += ord(badge)-96
    print(totaalprioriteit)


main()