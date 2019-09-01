import random
import time

def play_number_game():
    attempts = 0
    max_attempts = 5
    guess = -1
    number = random.randint(0, 100)
    correct = False

    while number != guess and attempts < max_attempts:
        attempts = attempts + 1
        rawInput = input("guess: ")
        try:
            guess = int(rawInput)
        except:
            print("EROOR")
            continue
        if guess < number:
            print("too small")
        elif guess > number:
            print("too big")
        else:
            correct = True
            print("right!")


    message = "FAIL"

    if not correct:
        for letter in message:
            print(letter)
            time.sleep(1)
        print("the correct number was " + str(number))

    warialbe = "quote"
    variavle = 'quote'


play = "yes"
while play == "yes":
    play_number_game()
    play = input("do u want to play again?").lower()
