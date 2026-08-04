#Python OOP
print("----------------------Without INIT---------------------")
class Student:
 pass
student1 = Student()
student2 = Student()
student1.name = "Harpreet"
student1.age = 20
student2.name ="Rahul"
student2.age = 18
print(student1.name, student1.age)
print(student2.name, student2.age)
print("-------------------------------------------------------")
#__init__ 
print("-----------------------With INIT-----------------------")
class Student:
 def __init__ (self,name,age):
  self.name = name 
  self.age = age
student1 = Student("Harpreet",20)
print(student1.name)
print(student1.age)
print("-------------------------------------------------------")
class car:
 def __init__(self,brand,color,year):
  self.brand = brand
  self.color = color
  self.year = year
car1 = car("BMW","Black",2028)
print(car1.brand,car1.color,car1.year)
print("-------------------------------------------------------")
 #Methods
print("------------------------Methods------------------------")
class Student:
 def __init__(self,name,age):
  self.name = name
  self.age = age
 def display(self):
  print("Name:",self.name)
  print("Age:",self.age)
student1 =Student("Harpreet",20)
student1.display()
print("-------------------------------------------------------")
#change_age method
print("----------------------change_age-----------------------")
class Student:
 def __init__(self,name,age):
  self.name = name
  self.age = age
 def display(self):
  print("Name:",self.name)
  print("Age:",self.age)
 def change_age(self,new_age):
  self.age = new_age
student1 =Student("Harpreet",20)
student1.change_age(21)
student1.display()
print("-------------------------------------------------------")

