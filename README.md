# Word Guessing Game

This is a simple word guessing game where the player tries to guess a random 5-letter word chosen from a predefined list.

## How to Play

1. **Setup:**
   - The game selects a random 5-letter word from a provided list of words.

2. **Game Loop:**
   - The player is prompted to enter their guess.
   - If the guess matches the selected word, the game congratulates the player and ends.
   - If the guess is not the correct length or not a valid word, the player is prompted to try again.
   - For valid 5-letter guesses:
     - Each letter in the guess is checked against the corresponding letter in the selected word.
     - If a letter matches both in position and character, it is highlighted in green.
     - If a letter exists in the selected word but not in the correct position, it is highlighted in red.
     - Letters that do not match are displayed normally.

3. **End of Game:**
   - The game ends when the player correctly guesses the word.

### Libraries Used

- `nltk`: Provides access to a corpus of English words.
- `random`: Used to select a random word from a list.
- `colorama`: Allows colored terminal output for better visual feedback.

