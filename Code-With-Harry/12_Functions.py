# Functions in Python

# Example 1 : 
def greetHello(name):
    print("Hello " + name)

print("Executing function......")
greetHello("Amith")
print("Done.")

# Example 2 : 
def letterGenerator(name):
    str = f"Hello, my name is {name} \n and I'm from India!!"
    print(str)

letterGenerator("Sidvin")

# Note : 1) Backticks/template literals(``) in Js is fstring(f"") in python
# 2) Escape sequence characters = \n

# Example 3 : 
def average(a, b):
    avg = (a + b) / 2
    return avg

print(f"The average is : {average(5,10)}")