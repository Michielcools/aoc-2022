import re
def main():
    file = open("input.txt", "r")
    input = ""
    pt = [0,0]
    ph = [0,0]
    visited = set({})
    lines = file.readlines()
    for line in lines:
        line = line.strip("\n")
        line = re.split(" ", line)
        i = 0
        while i < int(line[1]):
            input += line[0]
            i+= 1
    i = 0
    while i < len(input):
        if input[i] == "R":
            ph[0] += 1
        if input[i] == "L":
            ph[0] -= 1
        if input[i] == "U":
            ph[1] += 1
        if input[i] == "D":
            ph[1] -= 1
        i += 1
        xdif = ph[0] - pt[0]
        ydif = ph[1] - pt[1]
        if abs(xdif) > 1:
            pt[0] += xdif/2
            if abs(ydif) == 1:
                pt[1] += ydif
        if abs(ydif) > 1:
            pt[1] += ydif /2
            if abs(xdif) == 1:
                pt[0] += xdif
        visited.add(tuple(pt))
    print(len(visited))



if __name__ == '__main__':
    main()