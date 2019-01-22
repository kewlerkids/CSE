import random
import string
word_bank = ["Vanilla Bean", "Chocolate", "Pistachio", "Strawberry", "Rocky Road!", "Mint Chocolate Chip",
            "Coffee", "Cookies and Creme", "Do you like Ice cream?", "What is butter pecan?",
             "Espresso Chocolate Cookie Crumble", "Sea Salt Caramel Truffle"]

guess_word = random.choice(word_bank)

total_lives = 8
print("You have %s turns to start with" % total_lives)
print(list(string.ascii_letters))
guessed_letters = []

while total_lives > 0:
    players_guess = input("Letter?")

    string1 = guess_word
    list1 = list(string1)
    print("".join(list1))
    correct_letters = (list(string1))

    blanks = '_' * len(guess_word)
    print(blanks)
    for i in range(len(guess_word)):
        if guess_word[i] in correct_letters:
            blanks = blanks[:i] + guess_word[i] + blanks[i + 1:]

        else:
            total_lives -= 1

    print("You have %s lives left" % total_lives)

