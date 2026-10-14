import random
import time

# ---------- Settings ----------
DEBUG_SECRET = 42  # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 6       # Seconds allowed in Time Challenge mode


# Count How many attempts it takes a human to win
attempts = 0

# This variable is the result for this round: True -> You won; False -> You lost
win = False


print("Welcome to the Number Guessing Game")




# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.
difficulty_level = input("Enter a difficulty level for your game: easy -> 1, medium -> 2 or hard -> 3: ")

# Make a hash-map with the valid options for difficulty level
valid_difficulties = {"1": "Easy", "2": "Medium", "3": "Hard"}

# Keep on prompting the user to enter a valid difficulty level
while difficulty_level not in valid_difficulties:
    print(f"{difficulty_level} is not a valid difficulty level.")
    difficulty_level = input("Please enter a difficulty level for your game: easy -> 1, medium -> 2 or hard -> 3: ")

print(f"\n{valid_difficulties[difficulty_level]} Level Difficulty Chosen")
# Set a range dictionary based on difficulty level
# maps: difficulty_level -> [min_element, maximum_element]
RANGE = {
    "1": [1, 50],
    "2": [1, 100],
    "3": [1, 500],
}

# Set maximum number of attempts for a user based on difficulty level
# maps: difficulty_level -> maximum_no_of_attempts
MAX_ATTEMPTS = {
    "1": 10,
    "2": 8, 
    "3": 10,
}

minimum_number, maximum_number = RANGE[difficulty_level]
maximum_attempts = MAX_ATTEMPTS[difficulty_level]
    
# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.
game_mode = input("Enter a difficulty level for your game: Classic -> 1, Time Challenge -> 2: ")
valid_game_modes = {"1": "Classic", "2": "Time Challenge"}

while game_mode not in valid_game_modes:
    game_mode = input("Please enter a difficulty level for your game: Classic -> 1, Time Challenge -> 2: ")

print(f"\nYou have chosen {valid_game_modes[game_mode]} game mode")

# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.
if DEBUG_SECRET is not None:
    COMPUTER_PICK = DEBUG_SECRET
else:
    COMPUTER_PICK = random.randint(minimum_number, maximum_number)

if game_mode == "2":
    print("Your time begins now.")
    start_time = time.time()
# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.

# A while loop that ends when the user finishes all attempts or if the user wins.
while attempts < maximum_attempts and not win:
    print("-" * 100)
    print(f"\nYou have {maximum_attempts - attempts } attempts remaining.\n")
    
    if game_mode == "2":
        elapsed_time = time.time() - start_time
        time_remaining = TIME_LIMIT - elapsed_time
        print(f"\nYou have {time_remaining:.2f} seconds remaining.\n")

    human_guess = input(f"Enter a number between {minimum_number} and {maximum_number}.  ")

    # This loop ends as soon as the human enters a valid number inside the range.
    # We are using this loop so that we are not counting invalid human guesses in the number of attempts.
    while True:
        # Check if the human guess is a number, if it is a number, check if it is within the range
        if not str(human_guess).isdigit() or int(human_guess) < minimum_number or int(human_guess) > maximum_number:
            human_guess = input(f"Please enter a number between {minimum_number} and {maximum_number}.  ")

        # Else case -> Valid human guess.
        else:
            # Since this is a valid guess, increase number of attempts
            attempts += 1
            # Convert human guess from string -> integer
            human_guess = int(human_guess)
            # Exit the while loop
            break

    if game_mode == "2":
        elapsed_time = time.time() - start_time
        if elapsed_time > TIME_LIMIT:
            print("You ran out of time!")
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
else:
    print(f"You Lost! Try again on a lower difficulty.")
    print(f"The secret number was {COMPUTER_PICK}")