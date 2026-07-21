students = []
print("===============================================")
print("           Student Management System           ")
print("===============================================")
print("1. Add Student")
print("2. View Stuudents")
print("3. Exit")
choice = int(input("Enter your choice: "))
if choice ==1:
    students_name=input("Enter Studeent Name: ")
    students_age=int(input("Enter Studeent Age: "))
    print(students_name)
    print(students_age)
    student = {"name":students_name,"age": students_age} 
    students.append(student)
    print("Student added successfully")  
elif choice ==2:
    print()
elif choice ==3:
    print()   
else:
    print("Invalid input")
  