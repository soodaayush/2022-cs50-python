# from cs50 import get_int

# def main():
#     height = get_height()
#     for i in range(height):
#         print("#")
    

# def get_height():
#     while True:
#         try:
#             n = int(input("Height: "))
#             if n > 0:
#                 break
#         except ValueError:
#             print("That is not an integer!")
#     return n

# main()

# for i in range(4):
#     print("?", end="")

for i in range(3):
    for j in range(3):
        print("#", end="")
    print()