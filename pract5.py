import math
from graphics import *


def greet(name):
    return f"Hello, {name}!"


def product(a, b):
    return a * b


def main():
    myName = input("What is your name? ")
    greeting = greet(myName)
    print(greeting)

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = product(num1, num2)
    print(f"{num1} x {num2} = {result}")


def calcFutureValue(amount, years):
    interestRate = 0.065
    for year in range(years):
        amount = amount * (1 + interestRate)
    return amount


def futureValue():
    amount = float(input("Enter an amount to invest: "))
    years = int(input("Enter the number of years: "))
    final = calcFutureValue(amount, years)

    output = f"Investing £{amount:0.2f} for {years} years "
    output += f"results in £{final:0.2f}."
    print(output)


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
