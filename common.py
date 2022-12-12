"""
    Module Common

        consits most common funtion which can be used in any project

    Functions:

        is_prime(num) -> Return True if number is prime Else False
        is_even(num)  -> Return True if number is even else return False
        factorial(num) -> Return Factorial Value of a number
"""
import math
import sys

def is_prime(num: int)->bool:
    """
    Return True if number is prime Else False
    """
    try:
        if num <= 1:
            raise ValueError("Invalid Number!")
    except ValueError as err:
        print(f"!!Error!!{err}")
        sys.exit(1)
    if num in [2, 3, 5, 7, 11, 13]:
        return True

    if num%2==0:
        return False

    for check in range(3, int(math.sqrt(num))+2, 2):
        if num%check==0:
            return False
    return True

def is_even(num):
    "Return True if number is even else return False"
    return bool(num%2==0)

def factorial(num):
    "Return Factorial Value of a number"
    if num<=0:
        return 1
    ans = 1
    for value in range(2, num+1):
        ans *= value
    return ans

if __name__ == "__main__":
    # as script what should run
    print("It's a Module")
    print("is_prime(127) = ", is_prime(127))
    print("factorial(13)", factorial(13))
