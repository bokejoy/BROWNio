def mitmornin():
    print("This is Mit Morning class")


mitmornin()


def calculate():
    x = 7
    y = 10
    print(x + y)
    print(x * y)
    print(y / x)
    print(y - x)


calculate()


def majina(myfirstname, mylastname, age):
    print("My name is ", myfirstname, " ", mylastname, "", "I am", age, "years old.")


majina("Boke", "Gisira", "20")
majina("Tula", "Malaika", "23")
majina("Kirsten", "Nelly", "45")
majina("Timmy", "Kashy", "23")
majina("Kwashy", "Nicole", "23")


# create a func that is going to create average of a list
# [2.5 ,6 ,3 ,5]


def calculate_average(numbers):

    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

data = [2.5, 6, 3, 5]
result = calculate_average(data)
print("The average is", result  )

# func that gives the longest string in a list
str1="Hello everyone"
str2="Fine thankyou"
print(str1[0])
print(str2[3])
print(str2[10])
