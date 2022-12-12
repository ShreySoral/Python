import common
import os
import sys
#import common as cm
#from common import is_even, is_prime, factorial
#from common import *
#from common import is_even as check_even

#from . import common

def get_integer():
    """try to take a integer value input"""
    try:
        num = int(input("Enter a Integer Number: "))
        return num
    except ValueError:
        print("\nError!Invalid Input! Please Provide Only Integer Values\n")
        return get_integer()

if __name__ == "__main__":
    #NUM = get_integer()
    #print(check_even(NUM))
    # print(f"Is {NUM} Prime: {common.is_prime(NUM)}")
    # print(f"Factorial of Number {NUM} is {common.factorial(NUM)}")
    # print(f"Is number {NUM} Even - {common.is_even(NUM)}")
    for key in os.environ.keys():
        print(key)
    print(os.environ["USERNAME"])
    print(os.environ["HOMEPATH"])
    print(os.environ["PATH"])
    print('\n\n')
    print(sys.path)