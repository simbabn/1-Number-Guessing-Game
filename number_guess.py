import random

guess_number = random.randrange(1,10)

value = int(input("Chose a number between 1 and 10 : "))

while guess_number != value:
    if value < guess_number:
        print("is more")
        value = int(input("Enter number again: "))
    elif value > guess_number:
        print("is less")
        value = int(input("Enter number again: "))
    else :
        break
print("You find it!")
