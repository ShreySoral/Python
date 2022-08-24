file=open("name.txt")
name=file.read().strip()
file.close()
print(f"hello {name} welcome to python")