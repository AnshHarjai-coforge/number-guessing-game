import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

# Range sets the lower and upper bound for the guessing game
RANGE = [1, 50]

# Randomly pick a number from the range
COMPUTER_PICK = random.randint(RANGE[0], RANGE[1])

# Maximum number of attempts a user can make in one game.
NUM_ATTEMPTS = 10

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

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.