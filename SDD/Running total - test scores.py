#Running total - test scores

total = 0

for index in range(5):
    score = int(input("Please enter your test score:"))
    total = total + score

    print(total)