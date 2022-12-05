def main():
    file = open("input.txt", "r")
    file = file.readlines()
    i = 0
    while "1" not in file[i]:
        i+= 1
    aantal = file[i][-3]
    lijst = []
    teller = 0
    while teller < int(aantal):
        lijst.append([])
        teller += 1
    j = 0
    while j < i:
        k = 0
        while k < int(aantal):
            if file[j][k*4+1] != " ":
                lijst[k].append(file[j][k*4+1])
            k+=1
        j += 1
    i+=2
    while i < len(file):
        line = file[i]
        line = line.split(" ")
        amount = int(line[1])
        van = int(line[3])
        naar = int(line[5])
        while amount > 0:
            lijst[naar-1].insert(0,lijst[van-1][amount-1])
            lijst[van-1].pop(amount-1)
            amount -= 1
        i+=1
    for ding in lijst:
        print(ding[0])

main()