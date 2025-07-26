# Base class
class Animal:
    def move(self):
        print("Animal is moving...")

# Derived classes with different implementations of move()
class Dog(Animal):
    def move(self):
        print("Dog is walking 🐶")

class Fish(Animal):
    def move(self):
        print("Fish is swimming 🐟")

class Bird(Animal):
    def move(self):
        print("Bird is flying 🐦")

# Polymorphism in action
animals = [Dog(), Fish(), Bird()]

for animal in animals:
    animal.move()
