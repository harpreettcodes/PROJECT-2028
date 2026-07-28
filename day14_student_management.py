students = []
def add_student(students):
  students_name=input("Enter Student Name: ").strip()
  students_age=int(input("Enter Student Age: "))
  student = {"name":students_name,"age": students_age} 
  students.append(student)
  print("===================================================")
  print("              Student added successfully           ")  
  print("===================================================")
def view_students(students):
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
def search_student(students):
  search_name=input("Enter student name: ").strip()
  student=find_student(students,search_name)
  if student is not None:
   print("Student Found")
   print("--------------------------") 
   print("Name:",student["name"])
   print("Age: ",student["age"]) 
   print("--------------------------")
  else:
   print("===================================================")
   print("                  Student Not Found                ")
   print("===================================================")
def update_student(students):
 if not students:
  print("===================================================")
  print("                  No Students Found.               ")
  print("            Please add a student first.            ")
  print("===================================================")
  return # not (continue) cz it work only in loop. continue → skip to the next loop iteration.break → exit a loop.return → exit a function.
 inp=input("Enter student name you want to update: ").strip()
 student=find_student(students,inp)
 if student is not None:
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
   elif choice2 ==2:
    new_age=int(input("Enter new age: "))
    student["age"]= new_age
    print("===================================================")
    print("         Student age updated succesfully!          ")
    print("===================================================")
   elif choice2 ==3:
    new_name=input("Enter new name: ").strip()
    new_age=int(input("Enter new age: "))
    student["name"]= new_name
    student["age"]= new_age
    print("===================================================")
    print("         Student name updated succesfully!         ")
    print("         Student age updated succesfully!          ")
    print("===================================================")
    
 else:
  print("===================================================")
  print("                 Student Not Found                 ")
  print("===================================================") 
def delete_student(students):
 if not students:
  print("===================================================")
  print("                  No Students Found.               ")
  print("            Please add a student first.            ")
  print("===================================================")
  return
 inp2=input("Enter student name you want to delete: ").strip()
 student=find_student(students,inp2)
 if student is not None:
  students.remove(student)
  print("===================================================")
  print("          Student removed successfully!            ")
  print("===================================================")
 else:
   print("===================================================")
   print("               Student Not Found                   ")
   print("===================================================")
def find_student(students, name):
 for student in students:
   if name == student["name"]:
    return student
 return None
  
print("===================================================")
print("              Student Management System            ")
print("===================================================")
while True:
   print("===================================================")
   print("                  1. Add Student                   ")
   print("                  2. View Students                ")
   print("                  3. Search Student                ")
   print("                  4. Update Student                ")
   print("                  5. Delete Student                ")
   print("                  6. Exit                          ")
   print("===================================================")
   choice=int(input("Enter your choice: "))
   if choice ==1:
    add_student(students)
   elif choice ==2:
    view_students(students)  
   elif choice ==3:
     search_student(students)
   elif choice ==4:
     update_student(students)
   elif choice ==5:
    delete_student(students)
   elif choice ==6:
    print()
    break 
   else:
    print(" Invalid Input! ")
print("===================================================")
print("             Thanks For Using This Program         ")
print("===================================================") 
