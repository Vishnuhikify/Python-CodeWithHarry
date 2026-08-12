# List and List Methods

l1 = [1,23,5,6,7]

print(type(l1))
print(l1)

# To remove an element from the list
l1.remove(7)
print(l1)

# count
print(l1.count(23))

# Sort
l1.sort()
print(l1)

# To add an element into a list 
l1.append(10)
print(l1)

# To append multiple element at once
l1.extend([20,30,40])
print(l1)

# To add an element into a list 
l1.pop()
print(l1)

# To know the index of an element 
print(l1.index(10))

# List slicing : Excludes the last index
print("Slice : ", l1[0:3])

# List are mutable
l1[1] = "Amith"
print(l1)