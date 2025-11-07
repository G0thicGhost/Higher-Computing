#805 Task1

ownsAnIphone = [True, False, False, False, True, True, True, True]

count = 0
for index in range(len(ownsAnIphone)):
    if ownsAnIphone[index] == True:
        count = count + 1

print ("People who own an Iphone;",count)