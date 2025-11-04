import random


lines = []

for l in range(5):
    lotterynumbers = []
    for index in range(6):
        newnumber = random.randint(1,50)
        lotterynumbers.append(newnumber)
    lines.append(lotterynumbers)

    print(lines)

##

