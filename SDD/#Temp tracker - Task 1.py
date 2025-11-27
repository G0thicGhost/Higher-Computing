#Temp tracker - Task 1

totalTemps = 0
temps = []
for index in range(5):
    tempIn = int(input("Input a temperature between -20 and 50 please."))
    if tempIn > -20 or tempIn < 50:
        temps.append(tempIn)
    else:
        print("Error: Temperature was not between -20 and 50. D:")
        tempIn = int(input("Input a temperature between -20 and 50 please."))

for index in range(5):
    totalTemps = totalTemps + temps[index]

aveTemps = totalTemps/5

print(aveTemps)