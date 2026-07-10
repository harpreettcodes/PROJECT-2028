print("-------------FUN GUESS GAME-------------------")
secret = 4 
guess=int(input("Guess a number between 1-10:"))
while guess != secret :
 while guess <1 or guess >10:
  print("Invalid input! Please enter number between 1-10 only")
  guess=int(input("Guess a number between 1-10:"))
 if guess != secret:
  print("Oops Wrong guess! Try again")
  guess=int(input("Guess a number between 1-10:"))
print("WOW! you guessed it right")
print("THANKS FOR PLAYING")
print("------------------------------------------------")
  