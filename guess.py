import random
import time

# ---------- Settings ----------
DEBUG_SECRET = 42   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode
random.seed(DEBUG_SECRET)

# Range sets the lower and upper bound for the guessing game
RANGE = [1, 50]

# Randomly pick a number from the range
COMPUTER_PICK = random.randint(RANGE[0], RANGE[1])
print(COMPUTER_PICK)

# Maximum number of attempts a user can make in one game.
# NUM_ATTEMPTS = 10

# Count How many attempts it takes a human to win
attempts = 0

# This variable is the result for this round: True -> You won; False -> You lost
win = False


print("Welcome to the Number Guessing Game")




# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.

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
    
    attempts += 1
    print(f"\nThis is your {attempts} attempt\n")

    human_guess = input(f"Enter a number between {RANGE[0]} and {RANGE[1]}.  ")

    # This loop ends as soon as the human enters a valid number inside the range.
    # We are using this loop so that we are counting invalid human guesses in the number of attempts.
    while True:
        # Check if the human guess is a number, if it is a number, check if it is within the range
        if not str(human_guess).isdigit() or int(human_guess) < RANGE[0] or int(human_guess) > RANGE[1]:
            human_guess = input(f"Please enter a number between {RANGE[0]} and {RANGE[1]}.  ")

        # Else case -> Valid human guess.
        else:
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