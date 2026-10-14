# Number Guessing Game

## Testing Plan

| # | What I tested | What I did | Expected result | Actual result | Pass? |
|---|---|---|---|---|---|
| 1 | Input below the allowed range | Entered `0` | The game asks for a valid number without counting an attempt. | The game requested a valid number, and the attempt count did not increase. | Pass |
| 2 | Input above the allowed range | Entered `51` | The game asks for a valid number without counting an attempt. | The game requested a valid number, and the attempt count did not increase. | Pass |
| 3 | Non-numeric input | Entered `hello` | The game asks for a valid number without counting an attempt. | The game requested a valid number, and the attempt count did not increase. | Pass |
| 4 | Guess smaller than the secret number | Entered a valid number smaller than `DEBUG_SECRET` | The game indicates that the guess is too low and counts one attempt. | The game indicated that the guess was too low and counted one attempt. | Pass |
| 5 | Guess larger than the secret number | Entered a valid number larger than `DEBUG_SECRET` | The game indicates that the guess is too high and counts one attempt. | The game indicated that the guess was too high and counted one attempt. | Pass |
| 6 | Correct guess | Entered the same number as `DEBUG_SECRET` | The game displays a win message and the number of attempts used. | The game displayed a win message and the correct number of attempts. | Pass |
| 7 | Attempt counting with invalid inputs | Entered multiple out-of-range and non-numeric inputs | Invalid inputs do not increase the attempt count. | Invalid inputs did not increase the attempt count. | Pass |
| 8 | Empty input | Pressed Enter without entering anything | The game asks for a valid number without counting an attempt. | The game requested a valid number, and the attempt count did not increase. | Pass |
| 9 | Minimum range boundary | Entered `1` | The game accepts the input as a valid guess. | The game accepted `1` as a valid guess. | Pass |
| 10 | Maximum range boundary | Entered `50` | The game accepts the input as a valid guess. | The game accepted `50` as a valid guess. | Pass |

