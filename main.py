import random
import time

attempts = 0
max_attempts = 5
guess = -1
number = random.randint(0, 100)
correct = False

while number != guess and attempts < max_attempts:
    rawInput = input("guess: ")
    try:
        guess = int(rawInput)
    except:
        print("EROOR")
        continue
    attempts = attempts + 1
    if guess < number:
        print("too small")
    elif guess > number:
        print("too big")
    else:
        correct = True
        print("right!")

if not correct:
    print("F")
    time.sleep(1)
    print("A")
    time.sleep(1)
    print("I")
    time.sleep(1)
    print("L")
    time.sleep(1)
    print("the correct number was " + str(number))
