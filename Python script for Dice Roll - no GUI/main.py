import random

x = 'Y'

while (x == 'Y'):
    number = random.randint(1, 6)
    
    print("----------")
    if number == 1:
        print("|        |")
        print("|    0   |")
        print("|        |")

    if number == 2:
        print("|        |")
        print("| 0    0 |")
        print("|        |")

    if number == 3:
        print("|    0   |")
        print("|    0   |")
        print("|    0   |")

    if number == 4:
        print("| 0    0 |")
        print("|        |")
        print("| 0    0 |")

    if number == 5:
        print("| 0    0 |")
        print("|    0   |")
        print("| 0    0 |")

    if number == 6:
        print("| 0    0 |")
        print("| 0    0 |")
        print("| 0    0 |")

    print("----------")

    x = input("Roll again?")