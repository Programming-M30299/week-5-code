from graphics import *
import math


def greet(name):
    name = input("What is your name? ")
    return f"Hello, {name}!"


def product(a, b):
    return a * b


def main():
    myName = input("What is your name? ")
    greeting = greet(myName)
    print(greeting)

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    productResult = product(num1, num2)
    print(f"{num1} x {num2} = {productResult}")


def calcFutureValue(amount, years):
    interestRate = 0.065
    for year in range(years):
        amount = amount * (1 + interestRate)
    return amount


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
