import random


lotterynumbers = []
for index in range(6):
    newnumber = random.randint(1,50)
    lotterynumbers.append(newnumber)

print(lotterynumbers)

pos = random.randint(0,5)
print("Your lucky number this time is:",lotterynumbers[pos])