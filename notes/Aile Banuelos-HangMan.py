import random

word_bank = ["Vanilla Bean", "Chocolate", "Pistachio", "Strawberry", "Rocky Road!", "Mint Chocolate Chip",
            "Coffee", "Cookies and Creme", "Do you like Ice cream?", "What is butter pecan?",
             "Espresso Chocolate Cookie Crumble", "Sea Salt Caramel Truffle"]

guess_word = random.choice(word_bank)

total_lives = 8
print("You have %s turns to start with" % total_lives)


while total_lives > 0:
    players_guess = input("Letter?")

    string1 = guess_word
    list1 = list(string1)
    print("".join(list1))

    guessed_letters = []

    for character in list1:
        if character == "":
            current_index = list1.index(character)
            list1.pop(current_index)
            list1.insert(current_index, "*")

        # else character == 0:
            current_index = list1.index(character)
            total_lives -= 1

    print("You have %s lives left"% total_lives)
    # You have your word then it becomes a list of letters
    # and you have to see if the player guesses something in the list