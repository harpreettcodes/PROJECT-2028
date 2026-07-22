students = []
print("===============================================")
print("           Student Management System           ")
print("===============================================")

while True:
   print("1. Add Student")
   print("2. View Stuudents")
   print("3. Exit")
   choice=int(input("Enter 1 to add student,2 to view all students,3 to Exit: "))
   if choice ==1:
    students_name=input("Enter Studeent Name: ")
    students_age=int(input("Enter Studeent Age: "))
    student = {"name":students_name,"age": students_age} 
    students.append(student)
    print("Student added successfully")  
   elif choice ==2:
     print("=========Students=========")
     
     if not students:
       print("No Students Found.")
       print("Please add a student first.")
     else:
      for student in students:
       print("Name:",student["name"])
       print("Age: ",student["age"]) 
       print("--------------------------")
     print("==========================") 
   elif choice ==3:
    print()
    break 
   else:
    print(" Invalid Input! ")
print("===============================================")
print("          Thanks For Using This Program        ")
print("===============================================")


   