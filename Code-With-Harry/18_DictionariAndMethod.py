# Dictionary is like "objects" in JavaScript

# To declare an empty dictionary
dict1 = {}
print(dict1, type(dict1))

# To initialize a dictionary
dict2 = {
    "Amith": 100,
    "Varun": 1100,
    "Arjun": 100,
    "Harsh": 100
}

print(dict2)
print(dict2["Amith"])

# NOTE : Dictionaries are mutable

# To add key-value pair to an existing dictionary
dict2["Sidvin"] = 100
print(dict2)

# get method : This method doesn't returns error.
marks = dict2.get("Varun") # If there is no such key this method returns "None"
print(marks)

# To get all the keys and values : Returns the list of keys and values
print(dict2.keys())
print(dict2.values())

# items : returns the tuples of key value pair
print(dict2.items())