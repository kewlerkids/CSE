import random

word_bank = ["Vanilla Bean", "Chocolate", "Pistachio", "Strawberry", "Rocky Road!", "Mint Chocolate Chip",
            "Coffee", "Cookies and Creme", "Do you like Ice cream?", "What is butter pecan?",
             "Espresso Chocolate Cookie Crumble", "Sea Salt Caramel Truffle"]
guess_word = random.randint(word_bank)
length = len(word_bank)
print(length)
print(guess_word)

total_turns = 8
print("You have %s turns to start with" % total_turns)


