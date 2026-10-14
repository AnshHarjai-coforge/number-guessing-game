import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None  # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode


# If debug secret has a value, set the computer pick equal to it, otherwise keep it random.
# This is done for testing multiple computer guesses for manual testing
if DEBUG_SECRET is not None:
    COMPUTER_PICK = DEBUG_SECRET
else:
    COMPUTER_PICK = random.randint(RANGE[0], RANGE[1])

# Maximum number of attempts a user can make in one game.
# NUM_ATTEMPTS = 10

# Count How many attempts it takes a human to win
attempts = 0

# This variable is the result for this round: True -> You won; False -> You lost
win = False


print("Welcome to the Number Guessing Game")




# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.
difficulty_level = input("Enter a difficulty level for your game: easy -> 1, medium -> 2 or hard -> 3")

# Make a hash-set with the valid options for difficulty level
valid_difficulties = {"1", "2", "3"}

# Keep on prompting the user to enter a valid difficulty level
while difficulty_level not in valid_difficulties:
    print(f"{difficulty_level} is not a valid difficulty level.")
    difficulty_level = input("Please enter a difficulty level for your game: easy -> 1, medium -> 2 or hard -> 3")

# Set a range dictionary based on difficulty level
RANGE = {
    "1": [1, 50],
    "2": [1, 100],
    "3": [1, 500],
}

# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.

# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.

# A while loop that ends when the user wins.
while not win:

    # print(f"\nYou have {NUM_ATTEMPTS} attempts remaining.")
    # NUM_ATTEMPTS -= 1
    
    print(f"\nThis is your {attempts + 1 } attempt\n")

    human_guess = input(f"Enter a number between {RANGE[0]} and {RANGE[1]}.  ")

    # This loop ends as soon as the human enters a valid number inside the range.
    # We are using this loop so that we are not counting invalid human guesses in the number of attempts.
    while True:
        # Check if the human guess is a number, if it is a number, check if it is within the range
        if not str(human_guess).isdigit() or int(human_guess) < RANGE[0] or int(human_guess) > RANGE[1]:
            human_guess = input(f"Please enter a number between {RANGE[0]} and {RANGE[1]}.  ")

        # Else case -> Valid human guess.
        else:
            # Since this is a valid guess, increase number of attempts
            attempts += 1
            # Convert human guess from string -> integer
            human_guess = int(human_guess)
            # Exit the while loop
            break
    
    # Add logic to see if user's number is bigger, smaller, or equal than computer's guess
    if human_guess > COMPUTER_PICK:
        print("Your guess is bigger than computer's pick.")
    elif human_guess < COMPUTER_PICK:
        print("Your guess is smaller than computer's pick.")
    else:
        # Game is won now!
        win = True
    

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.
if win:
    print(f"You have won the game in {attempts} attempts!")