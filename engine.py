import random
def number():
    number = random.randint(0,10)
    guess = int(input("guess the number:"))
    print(number)
    if guess == number:
        print("wow! Correct")
    else:
        print("Wrong, try again")

