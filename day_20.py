#is_adult()
print("--------------------- is_adult() ----------------------")
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
student1 = Student("Harpreet",20)
student2 = Student("Aman",15)
student1.display()
print(student1.is_adult())
student2.display()
print(student2.is_adult())
print("-------------------------------------------------------")
#introduce()
print("-------------------- introduce() ----------------------")
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
      print("Name",self.name)
      print("Age:",self.age)
    def introduce(self):
      print(f"Hi, my name is {self.name} and I am {self.age} years old.")   
student1 = Student("Harpreet",20)
student1.display()
student1.introduce()
print("-------------------------------------------------------")