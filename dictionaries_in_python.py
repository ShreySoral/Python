# dictionary= a changeable, unordered collection of uniquw key:value pairs
#               Fast because they use hashing  and allow us to access a value quickly

capitals = {"USA": "Washington DC", "UK": "London",
            "India": "New Delhi", "France": "Paris", "Germany": "Berlin","Italy": "Rome"}


# print(capitals["India"])

print(capitals.get("Germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.update({"Iran":"Teheran"})
capitals.pop("USA")
print(capitals)
capitals.clear()
print(capitals)

for key,value in capitals.items():
    print(key,value)