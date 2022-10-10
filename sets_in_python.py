# set is a collection which is unordered, unindexed. No duplicate values

utensils={"fork","spoon","knife","spoon"}
utensils.add("napkin")
utensils.remove("spoon")
# utensils.clear()
print(utensils)
dishes={"bowl","plate","cup","knife"}
# print(utensils.difference(dishes))
# print(utensils.discard("fork"))
# print(utensils.intersection(dishes))
# print(utensils.isdisjoint(dishes))
# print(utensils.union(dishes))
# print(utensils.issubset(dishes))
# print(utensils.issuperset(dishes))
# print(utensils.pop())
# utensils.update(dishes)
print(utensils)
# for x in utensils:
#     print(x)

dinner_table=utensils.union(dishes)
# print(dinner_table)
# for x in dinner_table:
#     print(x)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))