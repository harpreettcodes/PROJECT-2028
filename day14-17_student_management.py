students=[]
def add_student(students):
  students_name=input("Enter Student Name: ").strip()
  try:
   students_age=int(input("Enter Student Age: "))
  except:
   print("Invalid input! Please enter a number.")
   return
  student = {"name":students_name,"age": students_age} 
  students.append(student)
  save_students(students)
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
   try:
    choice2=int(input("Please Select choose one from above: "))
   except:
    print("Invalid input! Please enter a number.")
    return
   if choice2 == 1:
    new_name=input("Enter new name: ").strip()
    student["name"]= new_name
    save_students(students)
    print("===================================================")
    print("          Student name updated succesfully!        ")
    print("===================================================")
   elif choice2 ==2:
    try:
     new_age=int(input("Enter new age: "))
    except:
     print("Invalid input! Please enter a number.")
     return
    student["age"]= new_age
    save_students(students)
    print("===================================================")
    print("         Student age updated succesfully!          ")
    print("===================================================")
   elif choice2 ==3:
    new_name=input("Enter new name: ").strip()
    try:
     new_age=int(input("Enter new age: "))
    except:
     print("Invalid input! Please enter a number.")
     return
    student["name"]= new_name
    student["age"]= new_age
    save_students(students)
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
  save_students(students)
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
def save_students(students):
  with open("student.txt","w")as file:
   for student in students:
    file.write(student["name"]+","+str(student["age"])+"\n")
def load_students():
 students=[]

 try:
  with open("student.txt","r")as file:
   lines=file.readlines()
   for line in lines:
    part=line.split(",")
    student={"name":(part[0]),
             "age":int(part[1].strip())}
    students.append(student)
 except FileNotFoundError:
  pass
 return students
students = load_students()
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
   try:
    choice=int(input("Enter your choice: "))
   except:
    print("Invalid input! Please enter a number.")
    continue
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
    print("Invalid choice! Please select 1, 2,3,4,5 or 6")
print("===================================================")
print("             Thanks For Using This Program         ")
print("===================================================") 
