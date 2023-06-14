from graphics import *
import math

# `product` function that has two parameters `a` and `b` and returns their product
def product(a, b):
    return a * b


# `divide` function that has two parameters `a` and `b` and returns their quotient
def divide(a, b):
    return a / b


# `main` function that takes two numbers and outputs their product and quotient
def main():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    productResult = product(num1, num2)
    divideResult = divide(num1, num2)
    print("{0} times {1} is {2}.".format(
        num1, num2, productResult))
    print("{0} divided by {1} is {2}.".format(
        num1, num2, divideResult))

# `greet` function that has a parameter `name` and returns a greeting
def greet(name):
    return "Hello, {0}!".format(name)

# `calcFutureValue` function has two parameters `amount` and `years`, returns the future value of the investment
def calcFutureValue(amount, years):
    interestRate = 0.065
    for year in range(years):
        amount = amount * (1 + interestRate)
    return amount


# `futureValue` function that takes an amount and number of years and outputs the future value of the investment
def futureValue():
    amount = float(input("Enter an amount to invest: "))
    years = int(input("Enter the number of years: "))
    finalValue = calcFutureValue(amount, years)
    print("Investing GBP {0:0.2f} for {1} years".format(amount, years),
          "will result in GBP {0:0.2f}.".format(finalValue))

# For exercises 1 and 2
def areaOfCircle(radius):
    return math.pi * radius ** 2


# For exercise 3
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)


def drawBrownEyeInCentre():
    window = GraphWin()
    # Add your code here


# For exercise 5
def drawBrownEye(win, centre, radius):
    pass
    # Remove pass and add your code here