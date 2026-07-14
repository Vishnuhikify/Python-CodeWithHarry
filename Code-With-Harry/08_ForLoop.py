# For Loop

# Example 1 : 
for i in range(5):
    if(i == 2):
        break
    print(i)

# Example 2 :
name = ["Amith", "Varun", "Sidvin", "Nitish", "Arvind"]

for name in name:
    print(name)

# Example 3 : 
a = {1,2,3,4, 5}

for num in a:
    if(num == 3):
        continue
    print(num)