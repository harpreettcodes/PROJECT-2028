class Student:
 def __init__(self,name,age):
  self.name = name
  self.age = age
 def display(self):
  print("Name:",self.name)
  print("Age:",self.age)
 def is_adult(self):
  if self.age >= 18:
   return True
  else:
   return False
 def update_name(self,new_name):
  self.name = new_name
students_name = input("Enter Student Name: ")
students_age = int(input("Enter Student Age: "))
student = Student(students_name,students_age)
student.display()
     