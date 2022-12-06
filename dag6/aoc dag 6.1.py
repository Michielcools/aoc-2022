def main():
    file = open("input.txt", "r")
    line = file.readlines()[0]
    i = 0
    checked = []
    while i < len(line):
        checked.append(line[i])
        if i > 3:
            checked.pop(0)
        if len(set(checked)) == 4:
            print(i+1)
            break
        i += 1





main()