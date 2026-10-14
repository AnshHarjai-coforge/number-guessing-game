# number-guessing-game
Testing Plan:
1. Enter a number out of the range in human_guess
2. Enter a character in human_guess
3. Enter a number less than debug_secret in human_guess which is within the range.
4. Enter a number more than debug_secret in human_guess which is within the range.
5. Enter the same number as debug_secret in human_guess.
6. Make sure attempts don't increase if I keep entering numbers outside the range, or non-numeric inputs.
7. Enter empty string in human_guess.
8. Check range minimum (1) and maximum (50).
