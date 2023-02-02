# Abstraction

class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath in and one breath out")

    def eat(self):
        print("Non Nom Nom")

    def procreate(self):
        print("Find a mate")

    def move(self):
        print("Onwards and upwards")

cat = Animal()
cat.breathe()