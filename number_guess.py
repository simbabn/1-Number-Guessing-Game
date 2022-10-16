import random
print("Welcome to Guess Number Game !")

def try_err(u_guess,num):
    if u_guess < num:           
        print("It's more!")
        return False
    elif u_guess > num:
        print("It's less")
        return False
    else:  # u_guess == num
        print('You got it!')
        return True

def guess():
    guess_number = random.randint(1, 10)
    while True:
        while True:
            value = input('Chose a number between 1 and 10 : ')
            try:
                value = int(value)
                break
            except ValueError:
                print('Enter a valid number, try again!')
        if try_err(value, guess_number):
            break

guess()
