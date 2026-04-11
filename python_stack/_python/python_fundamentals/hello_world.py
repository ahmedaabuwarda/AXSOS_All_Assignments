print("Hello World!")
name = "Ahmed"
print("Hello", name, "!")
print("Hello " + name + "!")
num = 5
print("Hello " + str(num) + "!")

food_one = "Pizza"
food_tow = "Burger"
print("I love to eat {food_one} and {food_tow}".format(food_one=food_one, food_tow=food_tow))

print(f"I love to eat {food_one} and {food_tow}")

game = "new game of thrones series"
print(game.upper()) # capitalizes all letters
print(game.title()) # capitalizes the first letter of each word

print(game.split())

# print(game.join(""))

def greet(name):
    print(f"Hello {name}!")

greet("dd")