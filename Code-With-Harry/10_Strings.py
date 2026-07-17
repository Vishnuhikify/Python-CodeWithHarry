name = "Vishnu"
print(name)

# Slice in strings
print(name[0:3])
print(name[1:3])

# Note : Strings are immutable
newName = name[0:4]
print("New name : ", newName)

# Uppercase
print(name.upper())

# Capitalize
print(name.capitalize())

# To see how many times a single letter or substr is repeated
print(name.count("a"))

# To scheck if there is a number in the given string
print(name.isnumeric())

# Note : More on strings
a = "Vishnu"
a = 'Vishnu'
a = '''Vishnu''' # used for multiline printing

b = '''my name
is Vishnu, I'm a 
software Engineer!!!'''