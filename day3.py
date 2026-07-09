print("-------------------VOTING ELIGIBLITY CHECKER-------------------")
age = int(input("Enter your age:"))
if age >= 18:
 print("You are Eligible")
 voter_id=input("Do you have voter ID card? (YES/NO)").lower()
 while voter_id != "yes" and voter_id != "no" :
  print("Invalid input. Please enter yes or no only")
  voter_id=input("Do you have a voter id card ? (YES/NO)").lower()
 if voter_id=="yes":
   print("Great! you can vote")
 elif voter_id=="no":
   print("Please apply for a voter ID first")
else:
 print("sorry,you're not eligible")
 print("You need to need wait", 18 - age,"more years to vote" )
print()
print("THANK FOR USING MY PROGRAM")
print("----------------------------------------------------------------")