import re
def calcsize(dict, dir):
    size = 0
    for element in dict[dir]:
        if type(element) == int:
            size += element
        elif type(element) == str:
            size += calcsize(dict, element)
    return size

def main():
    file = open("input.txt", "r")
    file = file.readlines()
    dir = ["/"]
    tree = {"/":[]}
    i = 1
    while i < len(file):
        line = file[i]
        if line[0] == "$":
            line = re.split(" |\n",line)
            if line[1] == "cd":
                if line[2] != "..":
                    naam = ""
                    for ding in dir:
                        naam += ding
                    naam += line[2]
                    dir.append(line[2])
                    tree[naam] = []
                else:
                    dir.pop(-1)
        else:
            line = re.split(" |\n", line)
            naam = ""
            for ding in dir:
                naam += ding
            if line[0] == "dir":
                tree[naam].append(naam+line[1])
            else:
                tree[naam].append(int(line[0]))
        i += 1
    sizedict = {}
    for element in tree:
        sizedict[element] = calcsize(tree,element)
    sizereq = 30000000- (70000000 - sizedict["/"])
    delete = sizedict["/"]
    for element in sizedict:
        if sizedict[element] >= sizereq and sizedict[element] < delete:
            delete = sizedict[element]
    print(delete)






main()