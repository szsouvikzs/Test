# self keyword is mandatory for calling variables names into method
# instance and class variables have whole different purpose
# constructor name should be __init__
# new keyword is not required when you created object

# Classes are user defined blueprint of prototype

# methods, variables, constructor, etc


class Calculator:
    num = 100  # class variables
    # default constructor

    def __init__(self,a,b):
        self.firstNumber=a
        self.secondNumber=b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as a method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber


obj = Calculator(2, 3)  # syntax to create objects in python
obj.getData()
obj.num
print(obj.Summation())