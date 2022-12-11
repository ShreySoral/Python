import time
x = 10
y = 20
# x, y defined in global scope
# a python can be a module or it can behave like a script
# __name__ it print current scope name 
# Module Scope -> whenever we import python file -> scope name will be same as filename
# import two --> scope --> two [execute entire code of two.py] 
# Main Scope --> whenever we execute python file -> scope name will be same as __main__

def hello(name):
    # name is defined in local scope hence it is a local variable
    print("Hello My name is ", name)

class Person:
    # Person() -> constrcutor, ~Person() -> Destructor
    count = 0 # class variable / class scope
    def __init__(self, name):
        self.name = name
        # name is local variable, self.name is an instance variable
        # self is a object scope / instance scope
        # count is a class variable
        Person.count += 1
    def __del__(self):
        # __init__ -> constructor (Classname()) -> invoke automatically whenever a new object is created!
        # __del__ -> destructor (~Classname())-> invoke automatically whenever a object is deleted!
        Person.count -= 1
        print(f"deleting object {self.name} ...")
        del self
    def __str__(self):
        return f"Person({self.name})"

def func():
    p1 = Person("sachin")
    p2 = Person("rajat")
    print(p1)
    print(p2)
    print("Now exiting Local Scope")
    return p1
# above code will execute not matter what
# if you use this file as module or you use this file as script
# in both cases above will execute

# if we import this file like `import two` than the value of __name__ will be `two`
# if we execute this file like `python two.py` than the value of __name__ will be `__main__` 
if __name__ == "__main__":
    # this part of code will only run if you executes this file as main file
    print("Let's call functionS")  # x = 100, x = 500
    x = func()
    print("\nCan you see that local scope only holds till function calling")
    print(x)
    time.sleep(5)
    # p1 = Person("Sachin")
    # p2 = Person("Rajat")
    # print("Total no of objects of person class are ", Person.count)
    # p3 = Person("Shivani")
    # print(f"Now we have {Person.count} objects of Person Class")
    # p1 = 100 # Over-riding
    # print("Now count is ", Person.count)
    # print(p2)
    # print(p3)
    # del p3
    # print("This is how program works")
