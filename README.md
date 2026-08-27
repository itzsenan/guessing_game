# Guessing Game

Simple guessing game written in Python.

## How to run
```shell
git clone https://github.com/itzsenan/guessing_game
cd guessing_game
python main.py
```

## How to play

### Starting

At startup it prompts the user `Do you want to play? [Y/n]`.

- To play in regular mode, type anything other than "n".
- To play in optimal mode, type "o".
- To see stats, type "stats".

### Regular mode
1. On each round, guess a number between 1 - 100.
2. The program will tell you if you're guess is too high or too low.
3. With that information, update your guess.
4. Repeat until game ends.
5. Program prompts to play again.

### Optimal Mode
1. On each round, guess a number between 1 - 100.
2. The program will tell you if you're guess is too high or too low.
3. The program will also tell you the optimal guess, which is found from the formula below.
```math
\frac{\text{Highest guess so far } + \text{ Lowest guess so far}}{2}
```
4. With that information, update your guess.
5. Repeat until game ends.
6. Program prompts to play again.

### Statistics
1. After entering "stats" into the `Do you want to play? [Y/n]` prompt, it will open the stats menu.
2. To print all stats to the console, type "stats".
3. To clear all stats, type "clear".
4. To exit the program from stats menu, type "exit".
5. After every game, the statistics auto update.
6. The stastics are stored in `stats.json`.

### Exiting while playing
To exit the game while playing, just write `exit` into the terminal to exit the game completely.
