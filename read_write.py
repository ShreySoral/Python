""" Just a Demo to read write files"""
import os

HOME = os.environ["HOMEPATH"]
DIR = "Desktop"
FILENAME = "hello.txt"
PATH = os.path.join(HOME, DIR, FILENAME)

def read_write_file(PATH):
    if os.path.exists(PATH):
        print("File Already Exists!")
        file = open(PATH, "rt")
        content = file.read()
        print(content)
        file.close()
    else:
        file = open(PATH, "w")
        content = """
            Hello World! This is a Demo File
                Have Fun with File Handling
        """
        file.write(content)
        file.close()

if __name__ == "__main__":
    read_write_file(PATH)