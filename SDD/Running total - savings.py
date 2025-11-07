#Running total program

total = 0
for index in range(12):
    thismonth = int(input("Please enter total savings this month:"))
    total = total + thismonth

    print("£", total)