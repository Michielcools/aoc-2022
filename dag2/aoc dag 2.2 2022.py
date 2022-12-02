file = open("dag 2.txt", "r")
vertaal = {"X": -3,"Y":0,"Z":3}
enemyvertaal = {"A":1, "B":2, "C":3}
punten = {0:3, 1:1, 2:2, 3:3, 4:1}
totaalscore = 0
for line in file:
    enemygetal = enemyvertaal[line[0]]
    totaalscore += vertaal[line[2]] + 3 + punten[enemygetal + vertaal[line[2]]/3]
print(totaalscore)

