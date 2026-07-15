#Single loop pattern print
print("---------------Single loop pattern print--------------------")
letters = ["A", "B", "C", "D", "E"];
for i in range(1,6):
  print(letters[i-1]*i)
print("------------------------------------------------------------")
#Single loop reverse pattern print
print("-------------Single loop reverse pattern print--------------")
letters = ["A","B","C","D","E"];
for i in range(5,0,-1):
  print(letters[i-1]*i)
print("------------------------------------------------------------")
#Nested loop pattern print
print("----------------Nested loop pattern print-------------------")
letters = ["A","B","C","D","E"];
for i in range(6):
  for j in range(i):
   print(letters[j], end="")
  print()
print("------------------------------------------------------------")
#Nested loop reverse pattern print
print("------------Nested loop reverse pattern print---------------")
letters = ["A","B","C","D","E"];
for i in range(5,0,-1):
  for j in range(i):
   print(letters[j], end="")
  print()
print("------------------------------------------------------------")