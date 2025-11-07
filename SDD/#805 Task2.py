#805 Task2
petpurchased =  ["Dog", "Dog", "Cat", "Rabbit", "Hamster", "Cat", "Hamster", "Budgie"]
counter = 0
pet = "Hamster"
position = 0

for index in range(len(petpurchased)):
    if pet == petpurchased[index]:
        position = counter
    counter = counter + 1

print(position)