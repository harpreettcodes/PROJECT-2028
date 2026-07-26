students = []
print("===================================================")
print("              Student Management System            ")
print("===================================================")

while True:
   print("===================================================")
   print("                  1. Add Student                   ")
   print("                  2. View Stuudents                ")
   print("                  3. Search Student                ")
   print("                  4. Update Student                ")
   print("                  5. Delete Student                ")
   print("                  6. Exit                          ")
   print("===================================================")
   choice=int(input("Enter 1 to add student,2 to view all students,3 To search a student,4 To update student name or age: ,5 To delete student: ,6 To exit: "))
   if choice ==1:
    students_name=input("Enter Student Name: ").strip()
    students_age=int(input("Enter Student Age: "))
    student = {"name":students_name,"age": students_age} 
    students.append(student)
    print("===================================================")
    print("              Student added successfully           ")  
    print("===================================================")
   elif choice ==2:
     print("=========Students=========")
     
     if not students:
       print("===================================================")
       print("                  No Students Found.               ")
       print("            Please add a student first.            ")
       print("===================================================")
     else:
      for student in students:
       print("Name:",student["name"])
       print("Age: ",student["age"]) 
       print("--------------------------") 
   elif choice ==3:
       found = False
       search_student=input("Enter student name: ").strip()
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
        print("===================================================")
        print("                  Student Not Found                ")
        print("===================================================")
   elif choice ==4:  
       if not students:
              print("===================================================")
              print("                  No Students Found.               ")
              print("            Please add a student first.            ")
              print("===================================================")
              continue
       found = False
       inp=input("Enter student name you want to update: ").strip()
       for student in students:
        if inp == student["name"]:
         found = True
         print("1. Update Name")
         print("2. Update Age")
         print("3. Update Both")
         choice2=int(input("Please Select choose one from above: "))
         if choice2 == 1:
          new_name=input("Enter new name: ").strip()
          student["name"]= new_name
          print("===================================================")
          print("          Student name updated succesfully!        ")
          print("===================================================")
          break
         elif choice2 ==2:
          new_age=int(input("Enter new age: "))
          student["age"]= new_age
          print("===================================================")
          print("         Student age updated succesfully!          ")
          print("===================================================")
          break
         elif choice2 ==3:
          new_name=input("Enter new name: ").strip()
          new_age=int(input("Enter new age: "))
          student["name"]= new_name
          student["age"]= new_age
          print("===================================================")
          print("         Student name updated succesfully!         ")
          print("         Student age updated succesfully!          ")
          print("===================================================")
          break

       if found == False:
        print("===================================================")
        print("                 Student Not Found                 ")
        print("===================================================")
   elif choice ==5:
    if not students:
     print("===================================================")
     print("         Student name updated succesfully!         ")
     print("         Student age updated succesfully!          ")
     print("===================================================")
     continue
    found = False
    inp2=input("Enter student name you want to delete: ").strip()
    for student in students:
     if inp2 == student["name"]:
       found = True
       students.remove(student)
       print("===================================================")
       print("          Student removed successfully!            ")
       print("===================================================")
       break

    if found == False:
            print("Student Not Found")
   elif choice ==6:
    print()
    break 
   else:
    print(" Invalid Input! ")
print("===================================================")
print("             Thanks For Using This Program         ")
print("===================================================")