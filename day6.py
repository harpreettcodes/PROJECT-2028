#patter printer
print("---------------patter printer--------------------")
for z in range(6):
   print("*"*z)
print("-------------------------------------------------")
#pyramid program
print("---------------pyramid program-------------------")
for x in range(1,10,2):
 space = (9-x)//2
 print(" " * space + "*"*x)
print("-------------------------------------------------")
#reverse pyramid
print("---------------reverse pyramid-------------------")
for _ in range(9,0,-2):
 spaces = (9-_)//2
 print(" " * spaces + "*"*_)
print("-------------------------------------------------")
#character printer
print("---------------character printer-----------------")
name=input("Enter your name:")
for i in name:
    print(i)
print("-------------------------------------------------")
#Double character printer
print("------------Double character printer-------------")
name=input("Enter your name:")
for i in name:
    print(i*2)
print("------------------------------------------------")
#enumerate() example
print("------------enumerate() example-----------------")
name2=input("enter your name:")
for number,ch in enumerate(name2,start=1):
    print(f"{number}. {ch}")
print("------------------------------------------------")