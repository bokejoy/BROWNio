class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self):
        raise NotImplementedError("Child class must implement this method.")


class Dog(Animal):
    def speak(self):
        return "woof!"


class Cat(Animal):
    def speak(self):
        return "meow!"


class Donkey(Animal):
    def speak(self):
        return "neigh!"

#create a project
dog = Dog("Sasha", "White")
print(dog.name)
print(dog.color)
print(dog.speak())

cat = Cat("Malaika", "Black")
print(cat.name)
print(cat.color)
print(cat.speak())

donkey = Donkey("Yana", "Brown")
print(donkey.name)
print(donkey.color)
print(donkey.speak())
