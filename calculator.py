from cs50 import get_int

# try:
#     x = int(input("x: "))
# except: 
#     print("That is not an int!")
#     exit()
# try:
#     y = int(input("y: "))
# except:
#     print("That is not an int!")
#     exit()

# print(x + y)

x = get_int("x: ")
y = get_int("y: ")

z = x / y
print(f"{z:.50f}")