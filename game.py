import random

WORD_LIST = ["cat", "dog", "owl", "whale", "chinchilla"]

# Randomly selects a word from the list
def choose_word():
    return random.choice(WORD_LIST)

# Return updated guessed letters
def process_guess(word, guessed_letters, guess):
    guess = guess.lower()
    if guess in word:
        guessed_letters.add(guess)
        return True
    return False

# Return guessed letters and "_" for missing letters
def display_word(word, guessed_letters):
    return " ".join([c if c in guessed_letters else "_" for c in word])

def play_game():
    word = choose_word()
    guessed_letters = set()
    attempts = 7

    while attempts > 0:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").strip().lower()

        if process_guess(word, guessed_letters, guess):
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")

        if all(c in guessed_letters for c in word):
            print(f"Great job! :) You guessed the word: {word}")
            return True

    print(f"Game over! :( The word was: {word} ")
    return False

if __name__ == "__main__":
    play_game()
