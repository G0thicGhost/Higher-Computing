
# Establishing record --------------------------------------------
from dataclasses import dataclass
@dataclass
class Order():
    orderNum : str = ""
    date : str = ""
    email : str = ""
    option : str = ""
    cost : float = 0.0
    rating : int = 0

# Subroutines------------------------------------------------------
def ReadFromFileIntoArrayOfRecords():
    items = []
    index = 0
    fileName = "SDD/NH_Computing-Science_Assignment-Electronic-Files_2025/orders.txt"
    orders = [Order() for index in range(505)]
    with open(fileName, "r") as readfile:
        line = readfile.readline().rstrip('\n')
        while line != "":
            items = line.split(",")
            orders[index].orderNum = items[0]
            orders[index].date = items[1]
            orders[index].email = items[2]
            orders[index].option = items[3]
            orders[index].cost = items[4]
            orders[index].rating = int(items[5])
            index = index + 1
            line = readfile.readline().rstrip('\n')
    return orders

def  FindPositionOfCustomer(orders):
    #2.1 Set position to -1
    position = -1
    #2.2 Set index to 0
    index = 0
    #2.3 Ask user to enter month to search for
    month = input("Enter month to search for")[0:3]
    #2.4 While position is -1 and index is less than the length of the array
    while position == -1 and index < len(orders):
        monthIndex = orders[index].date[3:6]
        #2.5 If current month is equal to searched month and current rating is 5 then
        if (monthIndex == month) and (orders[index].rating == 5):
            #2.6 Set position to index
            position = index
        #2.7 End if
        #2.8 Add 1 to index
        index = index + 1
    #2.9 End while

    #2.10 Return position
    return position

def WriteDetailsOfWinningCustomer(orders, position):
    writefileName = "SDD/NH_Computing-Science_Assignment-Electronic-Files_2025/winningCustomer.txt"
    #3.1 Open new file ‘winningCustomer.txt’
    with open(writefileName, "w") as writefile:
        # 3.2 If position is 0 or above then
        if position >= 0:
            # 3.3 Write winning order number, email and cost to ‘winningCustomer.txt’
            writefile.write(orders[position].orderNum+", "+orders[position].email+", "+str(orders[position].cost))
        # 3.4 Else
        else:
            # 3.5 Write ‘No winner’ to ‘winningCustomer.txt’
            writefile.write("No Winner.")
    # 3.6 End if
    # 3.7 Close ‘winningCustomer.txt’

def countOption(orders, thisOption):
    #counting occurences
    #set counter to 0
    counter = 0
    #loop for all items in list
    for index in range(len(orders)):
        # if item value meets condition then
        if orders[index].option == thisOption:
            #add 1 to counter
            counter += 1
    return counter



def DisplayOrders(orders):
    #4.1 Call countOption function to return the number of orders delivered
    noDelivered = countOption(orders,"Delivery")
    # 4.2 Call countOption function to return the number of orders collected
    noCollection = countOption(orders,"Collection")
    # 4.3 Output the total number of orders delivered
    print("Orders Delivered:", noDelivered)
    # 4.4 Output the total number of orders collect
    print("Orders Collected:", noCollection)
pass

#Main program -------------------------------------------------------------------
orders = ReadFromFileIntoArrayOfRecords()
position = FindPositionOfCustomer(orders)
WriteDetailsOfWinningCustomer(orders, position)
DisplayOrders(orders)
