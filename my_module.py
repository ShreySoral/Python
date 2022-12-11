"""
    It's a Demo Module File

    __name__ is a pre-define variable 
    which tell us about current scope
"""
class A:
    def hello(self):
        print("Hello From class A")

def laugh():
    print("ha ha ha ha "*5)

def cry():
    print("uuuaaa uaaaa uuaaa "*5)

def greet(name):
    print(f"Hello {name}, Welcome to Python Programming.")

if __name__ == "__main__":
    # this code only run when we execute this script
    print("the value of __name__ variable is", repr(__name__))
    laugh()
    greet("SACHIN")
    cry()