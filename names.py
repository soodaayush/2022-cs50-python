import sys

names = ["Thingy", "Dingus", "Daddy", "Mommy"]

if "Thingy" in names:
    print("Found")
    sys.exit(0)

print("Not found")
sys.exit(1)