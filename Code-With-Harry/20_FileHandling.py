# File handling in Python

# Writing to a file : Deletes the whole content and re-writes the file with the content entered as input to the file handling program

# # Way 1 : Writing to a file
# with open("test.txt", "w") as f:
#     f.write("My name is Amith B V, I'm a software Engineer!!")

# Way 2 : Writing to a file(Old Method)
# fp = open("test.txt", "w")
# fp.write("Good morning!!!")
# fp.close()

# ______________________________________________________

# Reading a file

# with open("test.txt", "r") as f:
#     data = f.read()
#     print(data)

# Old way of reading a file : 
# fp = open("test.txt", "r")
# data = fp.read()
# fp.close()

# ______________________________________________________

# Appending to a file
with open("test.txt", "a") as f:
    f.write("\nMy name is Amith")