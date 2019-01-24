import random
import string
word_bank = ["Vanilla Bean", "Chocolate", "Pistachio", "Strawberry", "Rocky Road!", "Mint Chocolate Chip",
            "Coffee", "Cookies and Creme", "Do you like Ice cream?", "What is butter pecan?",
             "Espresso Chocolate Cookie Crumble", "Sea Salt Caramel Truffle"]

guess_word = random.choice(word_bank)

total_lives = 8
print("You have %s turns to start with" % total_lives)
list(string.ascii_letters)
guessed_letters = ['?', '!', ' ']
blanks = list('_' * len(guess_word))
list_of_letters_in_guess_word = list(guess_word)

("".join(list_of_letters_in_guess_word))

for i in range(len(guess_word)):
    if guess_word[i] in guessed_letters:
        blanks[i] = list_of_letters_in_guess_word[i]

while total_lives > 0:
    print("".join(blanks))
    players_guess = input("Letter?")
    guessed_letters.append(players_guess)
    print("".join(guessed_letters))
    for i in range(len(guess_word)):
        if guess_word[i] in guessed_letters:
            blanks[i] = list_of_letters_in_guess_word[i]

    if total_lives == 0:
        print("You lost")

    if players_guess not in guess_word:
        total_lives -= 1

    print("You have %s lives left" % total_lives)
    print(" ")
