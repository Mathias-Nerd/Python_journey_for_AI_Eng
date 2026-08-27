# class Cup:
#     def __init__(self):
#         self.contents = "empty"


# my_cup = Cup()
# my_cup.contents = "Mocha"
# print(my_cup.contents)

# class Cup:
#     def greet(self):
#         print("Ready fo coffee")


# my_cup = Cup()
# my_cup.greet()


# class Cup:
#     def check_self(self):
#         print(self)


# my_cup = Cup()
# print(my_cup)
# my_cup.check_self()


# class CardboardCup:
#     def __init__(self, capacity):
#         self.capacity_ounces = capacity
#         self.contents_ounces = 0.0

#     def fill(self, ounces):
#         self.contents_ounces += ounces
#         print(f"Filled cupwith {ounces} ounces of coffee.")


# my_cup = CardboardCup(12.0)
# my_cup.fill(8.0)


# class Cup:
#     def __init__(self):
#         self.ounces = 0

#     def fill(self, amt):
#         self.ounces += amt


# my_cup = Cup()
# my_cup.fill(5)
# my_cup.fill(3)
# print(my_cup.ounces)


# class Cup:
#     def __init__(self):
#         self.ounces = 5

#     def drink(self, amt):
#         if amt > self.ounces:
#             print("Not enough liquid!")
#         else:
#             self.ounces -= amt


# my_cup = Cup()
# my_cup.drink(10)
# print(my_cup.ounces)

"""
Your Practice Exercise: The Pet Shelter
Write a Python class named Pet that fulfills the following requirements:
The Constructor (__init__):
It should accept three parameters: name, species, and age.
Store these parameters as instance attributes: self.name, self.species, and self.age.
Object Creation:
Create at least two different Pet objects (e.g., a dog and a cat) with their own unique names, species, and ages.
Output:
Print out the attributes of each pet to the console (for example, stating "My pet is a [species] named [name] who is [age] years old.").
Tip: Once you write your code, feel free to paste it here, and we can review it together before moving on to methods!
"""


# class Pet:
#     def __init__(self, name, species, age):
#         self.name = name
#         self.species = species
#         self.age = age


# pet1 = Pet("Max", "dog", 5)
# pet2 = Pet("Luna", "cat", 2)
# print(
#     f"My pet is a {pet1.species} named {pet1.name} who is {pet1.age} years old.")
# print(
#     f"My pet is a {pet2.species} named {pet2.name} who is {pet2.age} years old.")


"""
class TestCup:
    def __init__(self):
        print("Stamped")

cup_instance = TestCup()
"""


# class Cup:
#     def __init__(self, color):
#         self.color = color


# red_cup = Cup("red")
# print(red_cup.color)

class Cup:
    def fill(self):
        print("Pouring...")

class SuperCup(Cup):
    def fill(self):
        super().fill()
        print("Locking lid!")

sc = SuperCup()
sc.fill()