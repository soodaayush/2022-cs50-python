from cs50 import get_string

people = {
    "Carter": "911",
    "Dingbat": "902-383-1838"
}

name = get_string("Name: ")

if name in people:
    print(f"Number: {people[name]}")
