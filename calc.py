"""
    Module calc

        it is a basic calculation module which provide
        addition, multiplication, substraction, division features

    Classes

        This module does not contain any class

    Functions

        add(x, y) -> add x and y arguments and return result
        sub(x, y) -> subtract x and y arguments and return result
        ...

    Exit Status

        0 - Sucess
        1 - Zero Division Error
        2 - Invalid Input
        ...
"""

import sys   # script / program / source code

def add(num1, num2):
    """
        return num1+num2
    """
    return num1+num2

def sub(num1, num2):
    """
        return num1-num2
    """
    return num1-num2

def mul(num1, num2):
    """
        return num1*num2
    """
    return num1*num2

def div(num1, num2):
    """
        return num1*num2
    """
    try:
        result = num1/num2
    except ZeroDivisionError:
        print("!Error!Can not divide a number by zero")
        sys.exit(1) # status code / Exit Codes
    else:
        return result

while True:
    try:
        NUM1 = float(input("X: "))
        NUM2 = float(input("Y: "))
        break
    except ValueError:
        print("Error! Invalid Input! Please Provide int or float numbers as input")

if __name__ == "__main__":
    # entry point of script
    print("Addition: ", add(NUM1, NUM2))
    print("Substraction: ", sub(NUM1, NUM2))
    print("Multiplication: ", mul(NUM1, NUM2))
    print("Division: ", div(NUM1, NUM2))
    sys.exit(0)
