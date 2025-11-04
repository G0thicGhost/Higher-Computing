#805 Task3
petpurchased =  ["Dog", "Dog", "Cat", "Rabbit", "Hamster", "Cat", "Hamster", "Budgie"]
counter = -1
pet = "Hamster"
position = []

for index in range(len(petpurchased)):
    counter = counter + 1
    if pet == petpurchased[index]:
        position.append(counter)

print(position)