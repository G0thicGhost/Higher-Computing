#Temp tracker - Task 2

#set things
totalTemps = 0
temps = []
TEMP = 0

#loooooooop
for index in range(14):
    tempIn = float(input("Input a temperature between -20 and 50 please."))
    while tempIn < -20 or tempIn > 50:
        print("Error: Temperature was not between -20 and 50. D:")
        tempIn = float(input("Input a temperature between -20 and 50 please."))
    temps.append(tempIn)

for index in range(5):
    totalTemps = totalTemps + temps[index]
    #this works

avgTemps = totalTemps/5
#and this

print(avgTemps)