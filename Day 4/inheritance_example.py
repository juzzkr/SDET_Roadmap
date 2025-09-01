class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

# Inheritance
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Bruno")
cat = Cat("Kitty")

print(dog.speak())
print(cat.speak())
