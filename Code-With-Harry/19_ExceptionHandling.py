# Exception Handling in Python

try:
    a = int(input("Enter a number : "))
    print(a + 5)
except Exception as e:
    print("Somethin went wrong!! \nError : ", e)