import random

def get_random_word():
    words = ["apple", "banana", "orange", "grapes", "cherry"]
    return random.choice(words)

def display_current_status(guessed, guessed_letters, lives):

    sorted_letters = sorted(guessed_letters)
    print("\nUsed letters:", end=" ")
    for i in range(len(sorted_letters)):
        print(sorted_letters[i], end=", " if i < len(sorted_letters) - 1 else "")
    print()
    
    print(f"Lives left: {lives}")

    print("Current word:", end=" ")
    for ch in guessed:
        print(ch, end=" ")
    print()

def get_valid_guess(guessed_letters):
    while True:
        guess = input("Enter a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input!!\nPlease enter a single alphabet.")
        elif guess in guessed_letters:
            print("You've already guessed that letter.")
        else:
            return guess

def update_guessed_word(word, guessed, guess):
    for idx, char in enumerate(word):
        if char == guess:
            guessed[idx] = guess

def play_hangman():
    word = get_random_word()
    guessed = ['_'] * len(word)
    guessed_letters = set()
    lives = 6
    wrong_guesses = 0  # Count of wrong guesses

    print("*** Welcome to Hangman Game ***")
    print("Guess the word:")
    for ch in guessed:
        print(ch, end=" ")
    print()

    while lives > 0 and '_' in guessed:
        display_current_status(guessed, guessed_letters, lives)
        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print("Correct guess!")
            update_guessed_word(word, guessed, guess)
        else:
            lives -= 1
            wrong_guesses += 1
            print("Wrong guess!")

    if '_' not in guessed:
        print(f"\nCongratulations! You guessed the word: '{word}' with {wrong_guesses} incorrect guess{'es' if wrong_guesses != 1 else ''}")
    else:
        print(f"\nGame Over!!\nThe correct word was: '{word}'")

def main():
    while True:
        play_hangman()
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks to play Hungama Game")
            break

if __name__ == "__main__":
    main()