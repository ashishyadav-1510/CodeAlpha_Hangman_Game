# Hangman Game (Console Edition)
A fun, interactive command-line Hangman game written in Python. The player tries to guess a randomly selected word by suggesting letters one at a time. The game ends when the word is fully guessed or the player runs out of lives.

## Project Structure
hangman.py             # Main game script
README.md              # Project documentation

## How to Run the Game
1. Requirements
Python 3.x installed on your system
2. Run the script
From the terminal or command prompt, navigate to the script’s directory and run:
python hangman.py

## How to Play
You have 6 lives to guess the correct word.
You can only enter one letter at a time.
The game will:
Show which letters you've used
Show the number of lives left
Update the word display after every guess
If you guess the full word correctly before losing all lives, you win!

## Sample Words
The word is randomly selected from:
["apple", "banana", "orange", "grapes", "cherry"]
You can add more words to the words list in the get_random_word() function to increase the variety.

## Example Gameplay
*** Welcome to Hangman Game ***
Guess the word:
_ _ _ _ _

Used letters: a, e, t
Lives left: 3
Current word: _ a _ a _

Correct guess!
...
Congratulations! You guessed the word: 'grape' with 2 incorrect guesses.

## Replay Feature
After finishing a game, you’ll be prompted:
Do you want to play again? (y/n):
Type y to play again
Type n to quit

## Notes
Input is validated:
Only single letters are allowed.
Duplicate guesses are blocked.
Keeps track of wrong guesses and reports at the end.
Case-insensitive letter handling.

## Screenshot
### Code:
![image](https://github.com/ashishyadav-1510/CodeAlpha_Hangman_Game/blob/main/Screenshot/Screenshot%202025-07-19%20212750.png?raw=true)
![image](https://github.com/ashishyadav-1510/CodeAlpha_Hangman_Game/blob/main/Screenshot/Screenshot%202025-07-19%20212804.png?raw=true)

### Output:
![image](https://github.com/ashishyadav-1510/CodeAlpha_Hangman_Game/blob/main/Screenshot/Screenshot%202025-07-19%20212907.png?raw=true)

## Video
[Video](https://youtu.be/j6XIowYQHZM)

## Explaination:

import random
Imports the random module to allow selecting a random word from a list.

def get_random_word():
Defines a function that will return a random word for the player to guess.

    words = ["apple", "banana", "orange", "grapes", "cherry"]
A predefined list of possible words to choose from.

    return random.choice(words)
Selects and returns one random word from the list.

def display_current_status(guessed, guessed_letters, lives):
Displays the current game state: guessed letters, used letters, and lives left.

    sorted_letters = sorted(guessed_letters)
Sorts the guessed letters alphabetically for better readability.

    print("\nUsed letters:", end=" ")
Starts printing the used letters on the same line.

    for i in range(len(sorted_letters)):
        print(sorted_letters[i], end=", " if i < len(sorted_letters) - 1 else "")
Iterates through each guessed letter and prints it.
Adds commas between letters, but not after the last one.

    print()
Ends the line after printing all letters.

    print(f"Lives left: {lives}")
Displays the number of remaining lives.

    print("Current word:", end=" ")
Prints a label for the word-in-progress.

    for ch in guessed:
        print(ch, end=" ")
    print()
Prints the guessed word with underscores for unguessed letters (e.g., _ p p _ e).

def get_valid_guess(guessed_letters):
Prompts the player to input a valid letter that hasn’t already been guessed.

    while True:
        guess = input("Enter a letter: ").lower().strip()
Prompts the user, converts input to lowercase, and trims whitespace.

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input!!\nPlease enter a single alphabet.")
Checks if the input is a single alphabetic character; if not, shows an error.

        elif guess in guessed_letters:
            print("You've already guessed that letter.")
Prevents repeated guesses.

        else:
            return guess
Returns the valid guess.

def update_guessed_word(word, guessed, guess):
Updates the guessed list if the guessed letter is in the word.

    for idx, char in enumerate(word):
        if char == guess:
            guessed[idx] = guess
Iterates over the word; if the guessed letter matches a character, it replaces _ with that letter in the correct index.

def play_hangman():
Main function that controls a single round of the game.

    word = get_random_word()
Chooses a random word for the game.

    guessed = ['_'] * len(word)
Initializes the guessed word as a list of underscores (_) matching word length.

    guessed_letters = set()
Initializes an empty set to track guessed letters.

    lives = 6
Sets the number of allowed wrong guesses (lives).

    wrong_guesses = 0  # Count of wrong guesses
Counter to track how many guesses were incorrect.

    print("*** Welcome to Hangman Game ***")
    print("Guess the word:")
Welcomes the player and shows the initial masked word.

    for ch in guessed:
        print(ch, end=" ")
    print()
Prints the underscores representing the word to be guessed.

    while lives > 0 and '_' in guessed:
Main game loop: continues until lives run out or the word is fully guessed.

        display_current_status(guessed, guessed_letters, lives)
Shows the player’s progress so far.

        guess = get_valid_guess(guessed_letters)
Gets a new valid guess from the user.

        guessed_letters.add(guess)
Adds the guessed letter to the set of used letters.

        if guess in word:
            print("Correct guess!")
            update_guessed_word(word, guessed, guess)
If the guess is correct:
Show success message.
Update the guessed word to reveal the correct letters.

        else:
            lives -= 1
            wrong_guesses += 1
            print("Wrong guess!")
If the guess is wrong:
Subtract one life.
Increment the wrong guess counter.
Show failure message.

    if '_' not in guessed:
If there are no underscores left, the player guessed the word.

        print(f"\nCongratulations! You guessed the word: '{word}' with {wrong_guesses} incorrect guess{'es' if wrong_guesses != 1 else ''}")
Shows a win message with the number of wrong guesses (pluralized appropriately).

    else:
        print(f"\nGame Over!!\nThe correct word was: '{word}'")
If the player ran out of lives, print the losing message and reveal the word.

def main():
The main function that allows repeating the game.

    while True:
        play_hangman()
Runs the game once.

        again = input("\nDo you want to play again? (y/n): ").lower()
Asks the player whether they want to play another round.

        if again != 'y':
            print("Thanks to play Hungama Game")
            break
If the user does not type y, the game ends with a thank-you message.

if __name__ == "__main__":
    main()
Ensures that the main() function runs only when the script is executed directly (not imported).