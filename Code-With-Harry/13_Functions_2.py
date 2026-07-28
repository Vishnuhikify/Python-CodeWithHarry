# Functions

# Example 1 :
def func() -> None: 
    print("Hello, This is an empty function!!")
    
func()

# Example 2 : 
def greet(name: str, greetings: str = "Hello") -> None:
    print(f"{greetings}, {name}")
    return

greet("Vijaya!", "Hii")
greet("Vijaya!")

# Example 3 :
def add(a: float, b:float) -> float :
    print(f'Adding: {a} + {b}')
    sum = a + b
    return sum

res = add(4.5, 5.5)
print(res)