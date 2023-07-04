class fruits:
    def __init__(self, type, color, price, shape):
        self.fruittype = type
        self.fruitcolor = color
        self.fruitprice = price
        self.fruitshape = shape

    def display(self):
        print(self.fruittype, self.fruitcolor, self.fruitprice, self.fruitshape)


myobj=fruits("Watermelon", "green", 80, "circle")
myobj.display()

myobj=fruits("Orange", "orange", 25, "circle")
myobj.display()

myobj=fruits("Banana", "yellow", 20, "curve")
myobj.display()

