file = open("dag 2.txt", "r")
vertaal = {"X": 1,"Y":2,"Z":3}
enemyvertaal = {"A":1, "B":2, "C":3}
totaalscore = 0
enemyscore = 0
for line in file:
    for letter in line:
        if letter in enemyvertaal:
            enemyscore = enemyvertaal[letter]
        if letter in vertaal:
            totaalscore += vertaal[letter]
            if enemyscore == vertaal[letter]:
                totaalscore += 3
            if enemyscore - vertaal[letter] == -1 or enemyscore - vertaal[letter] == 2:
                totaalscore += 6
print(totaalscore)
