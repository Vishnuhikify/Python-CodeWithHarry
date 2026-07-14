# If-else statement

age = int(input("Enter your age : "))

if(age <= 18):
    if(age < 0):
        print("Invalid number, please enter correct age!!")
    else:
        print("NO, you cannot vote!")
else:
    print("YES, you can vote!")

# elif statement
# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")