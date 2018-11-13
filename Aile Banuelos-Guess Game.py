import random

number_guesses = 5
right_answer = random.randint(1, 10)
while number_guesses > 0:

    my_guess = input("What is the random number I have? ")
    my_guess = int(my_guess)

    if my_guess == right_answer:
        print("Correct!")
        break
    elif my_guess > right_answer:
        print("Try again, Too High.")
    elif my_guess < right_answer:
        print("Try again, Too low")

    number_guesses -= 1
