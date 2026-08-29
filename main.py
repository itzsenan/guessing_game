# Handles main guessing game, and prompts stats to write when needed
import math
import random
import sys

from stats import increase_stat, open_stats

# Starting variables
guessing = False

# Calculates optimal guess
def calculate_optimal(highest_guess: int, lowest_guess: int) -> int:
    return math.floor((highest_guess + lowest_guess) / 2)
    
# Game function
def guessing_game(optimal_mode: bool):
    if optimal_mode:
        print("------------ OPTIMAL MODE ------------")
    else:
        print("------------ REGULAR MODE ------------")

    setting_ints = True
    highest = 100

    while setting_ints:

        answer = input("Input the range of the guess.\nEtc: 100 for [1-100]: ")
        try:
            highest = int(answer)
            if highest < 1:
                print("The number has to be higher than 1.")
            else:
                setting_ints = False
                print(f"The range to guess is now: [1-{highest}]")
        except ValueError:
            if answer == "exit":
                print("Exiting game...")
                sys.exit()
            print("That's not a number!")

    print("--------------------------------------")

    # Set all variables
    rand_int = random.randint(1, highest)
    highest_guess = highest
    lowest_guess = 1
    guessed = False
    guesses = 0

    while not guessed:
        guessing = True

        while guessing:
            if optimal_mode:
                print(f"The optimal guess is {calculate_optimal(highest_guess, lowest_guess)}")

            guess = input(f"Guess a number. [1-{highest}] ")
            try:
                int_guess = int(guess)
                if int_guess > highest or int_guess < 1:
                        print("That number is not in the range!")
                else:
                    guessing = False
                    guesses += 1
            except ValueError:
                if guess == "exit":
                    print("Exiting game...")
                    sys.exit()
                print("That's not a number!")

        print("--------------------------------------")

        if int_guess == rand_int:
            print("============ GAME WINNER ============")
            print(f"You have guessed the correct number of {rand_int} in {guesses}!")
            print("=====================================")

            # Add 1 to stats win for that guesses amount
            increase_stat(guesses)
            
            # Game over, reset back to asking to play
            guessing = False
            ask_playing()
        elif int_guess < rand_int:
            print("Your guess is lower than the number!")
            lowest_guess = max(lowest_guess, int_guess)
        else:
            print("Your guess is higher than the number!")
            highest_guess = min(highest_guess, int_guess)

# Loop ask
def ask_playing():
    answer = input("Do you want to play? [Y/n] ").lower()

    if answer == "n":
        sys.exit()
    elif answer == "o": # Optimal mode
        guessing_game(True)
    elif answer == "stats":  # Shows stats
        open_stats()
    else:
        guessing_game(False)

def main():
    print("============ GUESSING GAME ============")
    ask_playing()

main()