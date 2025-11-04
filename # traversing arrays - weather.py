# traversing arrays - weather

averagetemp = 0
tempratures = [14, 12, 16, 20, 11, 18, 17]

for index in range(7):
    averagetemp = averagetemp + tempratures[index]
    
averagetemp = averagetemp/7
print(averagetemp)