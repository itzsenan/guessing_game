import random

def guessing_game():
    rand_int = random.randint(1, 100)
    guessed = False
    guesses = 0
    while not guessed:
        guessing = True
        while guessing:
                    try:
                        guess = int(input("Guess a number. [1-100]: "))
                        if guess > 100 or guess < 1:
                             print("That number is not in the range!")
                        else:
                            guessing = False
                            guesses += 1
                    except ValueError:
                        print("That's not a number!")

        if guess == rand_int:
            print(f"You have guessed the correct number of {rand_int} in {guesses}!")
            guessed = True
        elif guess < rand_int:
            print("Your guess is lower than the number!")
        else:
            print("Your guess is higher than the number!")
        print("-------------------------------")

playing = True
guessing = False
guessed = False

print("-------------------------------")
guessing_game()

while playing:
    answer = input("Do you want to play? [y, n]: ").lower()
    if answer == "n":
        playing = False
    else:
        guessing_game()
        print("-------------------------------")