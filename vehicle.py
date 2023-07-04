class Car:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def brand(self):
        raise NotImplementedError("Child class must implement this method.")


class Legacy(Car):
    def brand(self):
        return "Subaru"


class Serena(Car):
    def brand(self):
        return "Toyota"


class Impreza(Car):
    def brand(self):
        return "Subaru"


#create a project
legacy = Legacy("Black", "Legacy")
print(legacy.color)
print(legacy.name)
print(legacy.brand())

serena = Serena("White", "Serena")
print(serena.color)
print(serena.name)
print(serena.brand())

impreza = Impreza("Grey", "Impreza")
print(impreza.color)
print(impreza.name)
print(impreza.brand())




