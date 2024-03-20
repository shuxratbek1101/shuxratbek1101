import random
from logo_guess_num import logo
def game():
    print(logo)
    print("Welcome to the number guesssing game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty=input("Choose a difficulty.Type 'easy' or 'hard': ")
    easy_num=random.randint(1,100)
    attempt_num = 10
    if difficulty.lower()=="easy":
        while True:
            print(f"You have {attempt_num} attempts to guess a number ")
            guess=int(input("Make a guess\n>>>"))
            if attempt_num==1:
                print("You ran out of guesses")
                print("You lose!")
                break
            elif guess==easy_num:
                print("It's done!")
                break
            elif guess-easy_num>0:
                attempt_num-=1
                print("Too high")
                print("Guess again")
            elif easy_num-guess>0:
                attempt_num-=1
                print("Too low")
                print("Guess again")


    hard_num=random.randint(1,100)
    hard_attempt_num = 5
    if difficulty.lower()=="hard":
        while True:
            print(f"You have {hard_attempt_num} attempts to guess a number ")
            guess=int(input("Make a guess\n>>>"))
            if hard_attempt_num==1:
                print("You ran out of guesses")
                print("You lose!")
                break
            elif guess==easy_num:
                print("It's done!")
                break
            elif guess-easy_num>0:
                hard_attempt_num-=1
                print("Too high")
                print("Guess again")
            elif easy_num-guess>0:
                hard_attempt_num-=1
                print("Too low")
                print("Guess again")
respond=input("Do wou want to play 'the guess number' game? 'yes'or'no'")
if respond=="yes":
    game()
else:
    print("Goodbye")


