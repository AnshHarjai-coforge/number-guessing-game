# Number Guessing Game

## Testing Plan for classic game branch
1. Enter a number out of the range in human_guess
2. Enter a character in human_guess
3. Enter a number less than debug_secret in human_guess which is within the range.
4. Enter a number more than debug_secret in human_guess which is within the range.
5. Enter the same number as debug_secret in human_guess.
6. Make sure attempts don't increase if I keep entering numbers outside the range, or non-numeric inputs.
7. Enter empty string in human_guess.
8. Check range minimum (1) and maximum (50).

## Testing plan for difficulty-level branch
Test Plan for difficulty level:
1. Enter invalid difficulty levels -> strings, empty string, numbers except (1, 2, or 3), special characters.
2. Make sure that game ends after maximum_attempts is exhausted for each difficulty level.
3. Re-run most manual tests from classic game like boundary checking for range for each difficulty level.

## Testing plan for Time-Challenge branch
1. Enter invalid game modes -> strings, empty string, numbers except (1, 2, or 3), special characters.
2. Make sure that the timer is only activate when the user selects time challenge game mode.
3. Check if the user is able to win a game when the timer has expired even with a correct answer.
4. Test negative numbers in all inputs fields.

## Test Plan Observations
- All test cases passed, and all outputs were expected.