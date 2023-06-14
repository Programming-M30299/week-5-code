# `product` function that takes two numbers and outputs their product
# def product():
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(a * b)

# `product` function that has two parameters `a` and `b` and outputs their product
# def product(a, b):
#     print(a * b)

# `product` function that has two parameters `a` and `b` and returns their product
def product(a, b):
    return a * b

# `divide` function that takes two numbers and outputs their quotient
# def divide():
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     print(a / b)


# `divide` function that has two parameters `a` and `b` and outputs their quotient
# def divide(a, b):
#     print(a / b)


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

# `greet` function that takes a name and outputs a greeting
# def greet():
#     name = input("Enter your name: ")
#     print("Hello, {0}!".format(name))


# `greet` function that has a parameter `name` and outputs a greeting
# def greet(name):
#     print("Hello, {0}!".format(name))


# `greet` function that has a parameter `name` and returns a greeting
def greet(name):
    return "Hello, {0}!".format(name)


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
