import random

attempts = 0
max_attempts = 5
guess = -1
number = random.randint(0, 100)
correct = False

while number != guess and attempts < max_attempts:
    guess = int(input("guess: "))
    attempts = attempts + 1
    if guess < number:
        print("too small")
    elif guess > number:
        print("too big")
    else:
        correct = True
        print("right!")

if not correct:
    print("FAIL!")
    print("the correct number was " + str(number))
