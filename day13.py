#Dictionary creation
print("-------------------Dictionary creation---------------------")
student = {"name": "Harpreet","age": 20,"course": "BCA"}
print(student["name"])
print(student["age"])
print(student["course"])
print("-----------------------------------------------------------")
#Accessing values
print("-------------------Accessing values------------------------")
phone = {"brand":"mi","model":"latest","price":100000}
print(phone["brand"])
print(phone["model"])
print(phone["price"])
print("-----------------------------------------------------------")
#Updating values
print("--------------------Updating values------------------------")
car = {"brand": "Toyota","color": "White"}
car["color"]="Black"
print(car["color"])
print("-----------------------------------------------------------")
#Adding new keys
print("--------------------Adding new keys------------------------")
student = {"name": "Harpreet","age": 20}
student["course"] = "BCA"
print(student["name"])
print(student["age"])
print(student["course"])
print("-----------------------------------------------------------")
#Dictionary keys
print("--------------------Dictionary keys------------------------")
student = {"name": "Harpreet","age": 20,"course": "BCA"}
print(student.keys())
print("-----------------------------------------------------------")
#Dictionary values
print("--------------------Dictionary values----------------------")
student = {"name": "Harpreet","age": 20,"course": "BCA"}
print(student.values())
print("-----------------------------------------------------------")
#Dictionary item
print("----------------------Dictionary item----------------------")
student = {"name": "Harpreet","age": 20,"course": "BCA"}
print(student.items())
print("-----------------------------------------------------------")