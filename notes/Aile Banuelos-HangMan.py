import random

word_bank = ["Vanilla Bean", "Chocolate", "Pistachio", "Strawberry", "Rocky Road!", "Mint Chocolate Chip",
            "Coffee", "Cookies and Creme", "Do you like Ice cream?", "What is butter pecan?",
             "Espresso Chocolate Cookie Crumble", "Sea Salt Caramel Truffle"]

guess_word = random.choice(word_bank)
print(guess_word)

total_turns = 8
print("You have %s turns to start with" % total_turns)

while total_turns > 0:
    players_guess = input("Letter?")

    string1 = guess_word
    list1 = list(string1)
    print(list1)

    for character in list1:
        if character == "u":
            current_index = list1.index(character)
            list1.pop(current_index)
            list1.insert(current_index, "*")

        else character:
            current_index = list1.index(character)
            total_guess -= 1

    print("You have %s turns left"% total_turns)