# classes are user defined blueprint or prototype
# sum, multiplication, addition, constant
# methods, class variables, instance variables, constructor
from loops import summation


class Calculator:
    num = 100  # class variables

    # default constructor
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)  # syntax to create objects in Python
obj.getData()
print(obj.Summation())
print(obj.num)

obj1 = Calculator(44, 34)
obj1.getData()
print(obj1.Summation())
print(obj1.num)
