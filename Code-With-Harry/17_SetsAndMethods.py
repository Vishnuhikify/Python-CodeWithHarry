# Sets are mutable

a1 = {1,2,3,4,5,6,6,6,7}
a2 = {2,3,4}

# Clear method
# a1.clear()
# print(a1)
# print(a2)

# Pop Removes the first element
print(a1.pop())
print(a1)
print(a2)

# Add method
a1.add(20)
print(a1)

# Unions
print(a1.union(a2))

# Intersections
print(a1.intersection(a2))

# To create an empty set
a = set()
print(a, type(a))