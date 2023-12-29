import random

def choose_word():
    words = ["hangman", "python", "programming", "computer", "science", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 6
    incorrect_guesses = 0
    guessed_letters = []
    word_to_guess = choose_word()

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while incorrect_guesses < max_attempts:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            incorrect_guesses += 1
            print("Incorrect guess! Attempts left:", max_attempts - incorrect_guesses)
        else:
            print("Good guess!")

        print(display_word(word_to_guess, guessed_letters))

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

    if "_" in display_word(word_to_guess, guessed_letters):
        print("Sorry, you ran out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
