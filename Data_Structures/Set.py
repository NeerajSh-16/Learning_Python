# A type of collection
# It can be ordered or unordered
# All of its elements are unique

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {11,12,13,14,15,16,17,18,19,20}
set3 = {2,4,6,8,10,12,14,16,18,20}
set4 = {1,3,5,7,9,11,13,15,17,19}
print(set1)

set1.add(20)
print(set1)

set1.remove(20)
print(set1)

# we can also check if an element is present in a set or not

print(2 in set1)
print(20 in set1)

# Operations on sets ---> Union, intersection
# Union
print(set1 | set2)
print(set1.union(set2))
# Intersection
print(set1 & set3)
print(set1.intersection(set4))
print(set2 & set4)


