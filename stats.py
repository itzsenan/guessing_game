import json
import sys

FILE_PATH = "stats.json"
DEFAULT_JSON = {
  "less4": 0,
  "less6": 0,
  "less8": 0,
  "more7": 0
}

# Main JSON functions

def read_json() -> dict:
    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: {FILE_PATH} not found. \nCreating new file..")
        fix_json_file()
        print("Created new file. Please redo function.")
        sys.exit()

def write_json(data: dict):
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print(f"Error: {FILE_PATH} not found. \nCreating new file..")
        fix_json_file()
        print("Created new file. Please redo function.")
        sys.exit()

# Game functions

def increase_stat(guesses: int):
    if guesses < 4:
        stat = "less4"
    elif guesses < 6:
        stat = "less6"
    elif guesses < 8:
        stat = "less8"
    else:
        stat = "more7"

    # Find data and change stat
    data = read_json()
    data[stat] += 1
    write_json(data)

# Error handling
def fix_json_file():
    formated_default = json.dumps(DEFAULT_JSON, indent=2)
    with open(FILE_PATH, "w") as file:
        file.write(formated_default)

# Stats terminal interface

def print_stats():
    data = read_json()
    print("========== STATS MENU ==========")
    print(f"Less than 4: {data["less4"]}")
    print(f"Less than 6: {data["less6"]}")
    print(f"Less than 8: {data["less8"]}")
    print(f"More than 7: {data["more7"]}")
    print("================================")
    help_input()

def stats_help():
    print("Type `print` to print all stats.")
    print("Type `clear` to clear all stats.")
    print("Type `exit` to exit the program.")

def help_input():
    answer = input().lower()
    if answer == "exit":
        sys.exit()
        
    elif answer == "clear":
        answer = input("Are you sure? This cannot be undone. [y/N] ").lower()
        if answer == "y":
            fix_json_file()
            print("Cleared stats.")
            help_input()
            
    elif answer == "print":
        print_stats()
        
    else:
        stats_help() # If not entered valid command show list of commands and prompt input again
        help_input()

def open_stats():
    print("========== STATS MENU ==========")
    stats_help()
    print("================================")
    help_input()