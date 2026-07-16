print("-------------FUN GUESS GAME-------------------")
import random
secret = random.randint(1,10)
attempt = 0
guess=int(input("Guess a number between 1-10:"))
attempt += 1
while guess != secret :
 while guess <1 or guess >10:
  print("Invalid input! Please enter number between 1-10 only")
  guess=int(input("Guess a number between 1-10:"))
 if guess > secret:
  print("Too high!")
  guess=int(input("Guess a number between 1-10:"))
  attempt += 1 
 else:
  print("Too low!")
  guess=int(input("Guess a number between 1-10:"))
  attempt += 1
print("WOW! you guessed it right")
print("You guessed it in",attempt,"attempts")
print("THANKS FOR PLAYING") 
print("------------------------------------------------")
import random
f=int(input("How many times u want to roll dice= "))
for i in range(1,f+1):
 print("Dice Print",i,"=",random.randint(1,6))