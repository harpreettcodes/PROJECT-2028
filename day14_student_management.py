students = []
print("===============================================")
print("           Student Management System           ")
print("===============================================")

while True:
   print("1. Add Student")
   print("2. View Stuudents")
   print("3. Search Student")
   print("4. Exit")
   choice=int(input("Enter 1 to add student,2 to view all students,3 To search a student,4 To exit: "))
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
   elif choice ==3:
       found = False
       search_student=input("Enter student name: ")
       
       for student in students:
        if search_student == student["name"]:
         found = True
         print("Student Found")
         print("--------------------------") 
         print("Name:",student["name"])
         print("Age: ",student["age"]) 
         print("--------------------------")
         break 

       if found == False:
        print("Student Not Found")
   elif choice ==4:
    print()
    break 
   else:
    print(" Invalid Input! ")
print("===============================================")
print("          Thanks For Using This Program        ")
print("===============================================")


   