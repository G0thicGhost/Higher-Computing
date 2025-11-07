#File handling task 4

names = ["John","Joan","Mark","Michael"]
birthMonth = ["Jun", "Dec", "May", "Oct"]
ages = [23,35,23,8]

with open("SDD/File Handling/names.txt","w") as wfile:
    for counter in range(0,len(names)):
        wfile.write(names[counter] + ","+ str(ages[counter])+ ","+ str(birthMonth[counter]) +"\n")

# Run the program to see if it works. Now adapt the code slightly so that a third array (birth month) is added between lines 1 and 2 and also written to the CSV file.
