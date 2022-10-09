#  we can use indexing[] or slice() methods
# [start:stop:step]
# name="shrey soral"
# first_name=name[0:2]
# last_name=name[4:]
# funky_name=name[::3]
# reversed_name=name[::-1]
# print(name)
# print(funky_name)
# print(last_name)
# print(first_name)
# print(reversed_name)
website="http://google.com"
website1="http://wikipedia.com"
slice=slice(7,-4)
print(website[slice])
print(website1[slice])