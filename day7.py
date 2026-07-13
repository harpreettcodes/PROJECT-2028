#Nested for loops
print("------------------------Nested for loops--------------------------------------")
for i in range(1,4):
    print("Round", i)
    for j in range(2):
        print("Hello")
print("------------------------------------------------------------------------------")
#Printing Rows and Column
print("------------------------Printing rows and columns-----------------------------")
for i in range(5):
    for j in range(1, 4):
        print(j, end=" ")
    print()
print("------------------------------------------------------------------------------")
#single table
print("----------------------single table with one loop------------------------------")
table = 2
for i in range(1,6):
        print(table," X ",i," = ",i*table)
print("------------------------------------------------------------------------------")
# three tables together with space
print("----------------------three tables together with space------------------------")
for i in range(1,4):
 for j in range(1,4):
      print(i," X ",j," = ",i*j,)
 print()
print("------------------------------------------------------------------------------")