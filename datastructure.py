# list datastructure
# a list that enables you to change data
myclassmate = ["Nelly", "Faith", "Joy", "Austine"]
mynos = [4, 45, 3, -65, 7]
myclassmate[0] = "Nelly"
mynos.sort()
myclassmate.append("Mary")
myclassmate.insert(2, "Angela")
myclassmate.pop(0)

print(myclassmate)
print(mynos)
print(myclassmate[0])

myclassmate = ["Nelly", "Faith", "Joy", "Austine"]

name = ["Nelly", "Faith", "Joy", "Austine"]

for myclassmate in myclassmate:
    print(myclassmate)

# this is a tuple
countries = ("Tanzania", "Ghania", "Somalia", "Eritrea")
print(countries)

# sets datastructures
cars = {"Subaru", "Nissan", "Toyota", "Audi"}
print(cars)

# for loop
cars = {"Subaru", "Nissan", "Toyota", "Audi"}
for cars in cars:
    print(cars)

# dictionaries datastructure
matunda = {"price": 80, "color": "Green", "Name": "Watermelon"}

bei=matunda["price"]
print(bei)
print(matunda)

mandazi={"price":50, "color": "Brown", "Name":"Mahamri"}
print(mandazi)


drinks={"price":60, "color": "Green", "Name":"Club Soda Apple"}
print(drinks)

bei=matunda["price"]

print(bei)
