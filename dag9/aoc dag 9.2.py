import re
def main():
    file = open("input.txt", "r")
    input = ""
    p = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
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
            p[0][0] += 1
        if input[i] == "L":
            p[0][0] -= 1
        if input[i] == "U":
            p[0][1] += 1
        if input[i] == "D":
            p[0][1] -= 1
        i += 1
        move(p)
        visited.add(tuple(p[9]))
    print(len(visited))

def move(p):
    j = 1
    while j < 10:
        xdif = p[j-1][0] - p[j][0]
        ydif = p[j-1][1] - p[j][1]
        if abs(xdif) > 1:
            p[j][0] += xdif/2
            if abs(ydif) == 1:
                p[j][1] += ydif
        if abs(ydif) > 1:
            p[j][1] += ydif /2
            if abs(xdif) == 1:
                p[j][0] += xdif
        j+= 1


if __name__ == '__main__':
    main()