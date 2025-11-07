#File handling task 2

#-------------Main Program-----------------
import time
#open file
with open("SDD/File Handling/newfile.txt","w") as writefile:
    writefile.write("Emilia, Red, May")
    time.sleep(1)

# Run the program and see what it does, then adapt the code so that the program writes your full name, favourite colour and birth month to the file instead.