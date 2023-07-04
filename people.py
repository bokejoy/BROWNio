class people:

    def __init__(self, name, age, gender):
       self.personname = name
       self.personage = age
       self.persongender = gender

    def display(self):
        print(self.personname, self.personage, self.persongender)

myobj=people("Kwashy",20, "female")
myobj.display()

myobj=people("Kirsten",19, "female")
myobj.display()

myobj=people("Timmy", 19, "male")
myobj.display()
