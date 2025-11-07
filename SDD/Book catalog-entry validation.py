#Book catalog-entry validation
print("""1. Add Book
      2. View Catalog
      3. Search Books
      4. Exit""")
Option = int(input("What do you wish to view?"))

while Option <0 or Option >4:
    print("Error. That is not a number between 1 and 4, please try again.")
    Option = int(input("Please enter a correct numbe that corresponds to an option."))