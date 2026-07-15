#Nested loop alpha pattern
print("-----------Nested loop alpha pattern------------")
for i in range(1,6):
 for j in range(1,i+1):
  print(j,end=" ")
 print()
print("------------------------------------------------")
#Nested loop reverse alpha pattern
print("------Nested loop reverse alpha pattern---------")
for i in range(5, 0, -1):
  for j in range(i, 0, -1):
    print(j, end=" ")
  print()
print("-------------------------------------------------")
#
print("--------------Table on user demand---------------")
table =int(input("Enter your number= "))
for i in range(1,11):
  print(table," X ",i," = ",i*table)
print("-------------------------------------------------")
#
print("---------------------Sum-------------------------")
number = int(input("Enter your number= "))
total = 0
for i in range(1, number + 1):
    total += i 
print("Sum ->",total)
print("-------------------------------------------------")
#Factorial
print("-----------------Factorial-----------------------")
number = int(input("Enter your number= "))
total = 1
for i in range(1, number + 1):
    total *= i 
print("Factorial ->",total)
print("-------------------------------------------------")