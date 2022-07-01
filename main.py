import math


class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b

    @staticmethod
    def get_log(a):
        return math.log(a)

    @staticmethod
    def get_power(a, b):
        return a ** b


calc = Calculator()

while True:

    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Get logarithm")
    print("6: Get power")
    print("7: Exit")

    ch = int(input("Select operation: "))

    if ch in (1, 2, 3, 4, 5, 6, 7):

        if ch == 7:
            break

        if ch == 5:
            a = int(input("Enter your number: "))
            print("logarithm of", a, "=", calc.get_log(a))
            break

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if ch == 1:
            print(a, "+", b, "=", calc.add(a, b))
        elif ch == 2:
            print(a, "-", b, "=", calc.subtract(a, b))
        elif ch == 3:
            print(a, "*", b, "=", calc.multiply(a, b))
        elif ch == 4:
            print(a, "/", b, "=", calc.divide(a, b))
        elif ch == 6:
            print(a, "**", b, "=", calc.get_power(a, b))

    else:
        print("Invalid Input")
