import random

# Calculates optimal guess
def calculate_optimal(highest_guess, lowest_guess):
    return round(((highest_guess + lowest_guess) / 2), 0)

# Game function
def guessing_game(tell_optimal):
    print("-------------------------------")

    # Set all variables
    rand_int = random.randint(1, 100)
    highest_guess = 100
    lowest_guess = 1
    guessed = False
    guesses = 0

    while not guessed:
        guessing = True

        while guessing:
            if tell_optimal:
                print(f"The optimal guess is {calculate_optimal(highest_guess, lowest_guess)}")

            guess = input("Guess a number. [1-100]: ")
            try:
                intGuess = int(guess)
                if intGuess > 100 or intGuess < 1:
                        print("That number is not in the range!")
                else:
                    guessing = False
                    guesses += 1
            except ValueError:
                if guess == "exit":
                    print("Exiting game...")
                    exit()
                print("That's not a number!")

        if intGuess == rand_int:
            print(f"You have guessed the correct number of {rand_int} in {guesses}!")
            guessed = True
        elif intGuess < rand_int:
            print("Your guess is lower than the number!")
            if intGuess > lowest_guess:
                lowest_guess = intGuess
        else:
            print("Your guess is higher than the number!")
            if intGuess < highest_guess:
                highest_guess = intGuess
            
        print("-------------------------------")

# Starting variables
playing = True
guessing = False
guessed = False

while playing:
    answer = input("Do you want to play? [y, n]: ").lower()
    if answer == "n":
        playing = False
    elif answer == "o": # O for optimal
        guessing_game(True)
    else:
        guessing_game(False)
