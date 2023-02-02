# Object oriented programming (oop)

# Everything in OOP is an object and objects are modelled against real world objects.

# Classes are the templates we use to create objects.
# Classes are a way of bringing both data and functunality of our code together.

# Create a class

class Dog:

    animal_kind = "Canine" # class variable
    animal_kind2 = "Octupus"
    def bark(self): # method
        return "woof"

# self - I'm refering to the current class.

# print(Dog.animal_kind)
#print(Dog.bark())

# Instantiation of a class (Instantiation creating or making an object from a class)

fido = Dog()
lassie = Dog()

print(type(fido))
print(type(lassie))
print(fido.animal_kind)
print(lassie.animal_kind)
print(fido.bark())

Dog.animal_kind = "Dolphin"

print(fido.animal_kind) # Now
print(lassie.animal_kind)
print(lassie.animal_kind2)

# The dogs can still access their method
print(fido.bark)
print(lassie.bark())