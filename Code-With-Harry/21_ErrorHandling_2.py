# Error handling

# Example 1 : It's a bad practice
a, b = 10, '20'

# print(a + b) # Throws error

try: 
    print(a + b)
except Exception as error:
    print(f'Something went wrong: {error}')
    
print("Continuing.......")

# Example 2 : 
try: 
    print(a + b)
except TypeError as error:
    print(f'Please enter a number in the form of an integer or a float!!')
    
# Multiple Exception :
try: 
    print(a + b)
except TypeError as error:
    print(f'Please enter a number in the form of an integer or a float!!')
except Exception as error:
    print(f'Something else went wrong: {error}')
    
# Note : Don't use "Exception" in the beginning, because it absorbs all the errors