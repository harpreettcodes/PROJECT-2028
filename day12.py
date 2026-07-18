#remove function in list
print("------------------.remove()-----------------")
numbers = [10, 20, 30, 40]
numbers.remove(30)
print(numbers)
print("--------------------------------------------")
#pop function in list
print("--------------------.pop()------------------")
numbers = [5, 10, 15]
x = numbers.pop()
print(x)
print(numbers)
print("--------------------------------------------")
#for loop using list
print("-----------------loop list------------------")
animals = ["Cat", "Dog", "Rabbit"]
for animal in animals:
    print(animal)
print("--------------------------------------------")
#len function in list
print("------------------len()---------------------")
games = ["BGMI", "Minecraft", "Valorant"]
for i in range(len(games)):
    print(i, games[i])
print("--------------------------------------------")
#input + append + len + remove function
print("------------for i in range(len(list))-------")
games=[]
for z in range(5):
    game=input("Enter a game: ")
    games.append(game)
for i in range(len(games)):
    print(i,games[i])
r=input("Enter a game to remove: ").lower()
games.remove(r)
for j in range(len(games)):
    print(j,games[j])
print("--------------------------------------------")


