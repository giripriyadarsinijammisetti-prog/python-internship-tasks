import random

words = ["python", "apple", "tiger", "chair", "river"]
secret_word = random.choice(words)

print("Welcome to Hangman!")
print("The word has", len(secret_word), "letters")

guessed_letters = []
lives = 6
used_letters = []

while lives > 0:
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display = display + letter + " "
        else:
            display = display + "_ "

    print(display)
    print("Lives left:", lives)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in used_letters:
        print("You already tried that letter.")
        continue

    used_letters.append(guess)

    if guess in secret_word:
        print("Correct!")
        guessed_letters.append(guess)
    else:
        print("Wrong!")
        lives = lives - 1
    won = True
    for letter in secret_word:
        if letter not in guessed_letters:
            won = False

    if won:
        print("You won! The word was", secret_word)
        break

    if lives == 0:
        print("Game over! The word was", secret_word)