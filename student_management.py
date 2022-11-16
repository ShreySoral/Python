"""
    Student Management Project
    
        add_new_record(record) 
            add a new record to existing data file
        search_record(key)
            search and print particular students data
        show_result()
            will entire result
"""

import os
import time

def add_new_record(record):
    # record =  ["sachin", 80, 80, 80]
    record[-3:] = map(str, record[-3:])
    # record = ["sachin", "80", "80", "80"]
    line = "\n"+ ",".join(record)
    # line = "\nsachin,80,80,80"
    with open("records.csv", "a") as file:
        file.write(line)
        print("!Record Updated Sucessfully!")
    
def search_record(key):
    key = key.strip().lower()
    with open("records.csv", "r") as file:
        file.readline() # reading header
        for line in file:
            if line=="\n":
                continue
            # line = 'Sachin,80,70,60\n'
            line = line.strip().split(",")
            # line = ["Sachin", "80", "70", "60"]
            name = line[0].strip().lower()
            if name == key:
                per = sum(map(int, line[-3:]))/3
                print(f"       Name        =  {name}")
                print(f"       Maths       =  {line[1]}")
                print(f"       Chemistry   =  {line[2]}")
                print(f"       Physics     =  {line[3]}")

                print(f"\n      Percentage  = {per:.2f}")

                print("\n", "_"*50, "\n")
                
def show_result():
    with open("records.csv") as file:
        header = file.readline().strip().split(',')
        header.append("Percentage")
        # ["Name", "Maths", "Chemistry", "Physics", "Percentage"]
        #   | 15 |      10 |         10   |      10 |         10 |
        width = 61
        output = "|{:^15}|{:^10}|{:^10}|{:^10}|{:^10}|"
        print("-"*width)
        print(output.format(*header))
        print("-"*width)
        for line in file:
            if line=="\n":
                continue
            # line = 'Sachin,80,70,60\n'
            line = line.strip().split(",")
            # line = ["Sachin", "80", "70", "60"]
            line[0] = line[0].strip().title()
            per = sum(map(int, line[-3:]))/3
            per = f"{per:.2f}"
            line.append(per)
            # line = ["Sachin", "80", "70", "60", "70.00"]
            print(output.format(*line))
            print("_"*width)
            
        
if __name__ == "__main__":
    # execution of code will start from here
    while True:
        os.system("cls") # macos/linux -> "clear"
        time.sleep(2)
        print("\n\n\n\n")
        print("Welcome Student Management Project".center(100, "_"))
        print("\n\n\n\n")
        
        menu = """
        1. Add Record
        2. Search Record
        3. Show Result
        4. Exit
        """
        print(menu)
        
        choice = input("Your Choice: ".rjust(30))
        time.sleep(5)
        if choice=="1":
            name =  input("Enter Student Name    : ".rjust(30))
            maths = input("Enter Maths Marks     : ".rjust(30))
            chem  = input("Enter Chemistry Marks : ".rjust(30))
            phy   = input("Enter Physics Marks   : ".rjust(30))
            record = [name, maths, chem, phy]
            add_new_record(record)
            time.sleep(5)
        elif choice=="2":
            name = input("Enter Student Name: ".rjust(30))
            search_record(name)
            input("\n\n\nPress Enter to Continue ")
            # search record
        elif choice=="3":
            show_result()
            input("\n\n\nPress Enter to Continue ")
        elif choice=="4":
            # exit
            print("\n\n\n\n")
            print("Thank you For Using Student Management Project".center(100))
            print("\n\n\n\n")
            time.sleep(5)
            os.system("cls")
            exit(0)
        else:
            print("\n\n\n")
            print("Error! Invalid Choice Try Again".center(50))
            time.sleep(5)
        
    