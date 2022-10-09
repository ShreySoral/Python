# tuple=collection which is ordered and immutable it is used to group together related data

student=("bro",21,"male")
print(student.count("bro"))
print(student.index("male"))

for x in student:
    print(x)

if "bro" in student:
    print("bro is in the tuple")