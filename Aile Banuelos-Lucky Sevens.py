import random

# Balance of money

total_dollars = 15
max_money = 15

print("Balance: %s" % total_dollars)
print("You need seven to win.")
print("You bet 1 dollar.")
print("")

lucky7 = 7
total_rounds = 0

# The game

while total_dollars > 0:

    # Rolling the dice

    print("You rolled...")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(dice1, dice2)
    print("Added together they make...")
    dice_total = dice1 + dice2
    print(dice_total)
    total_dollars -= 1

    # Gain or lose money

    if dice_total == lucky7:
        print("Nice Roll! Here's 4$")
        total_dollars += 5
        print("Balance: %s" % total_dollars)
        total_rounds += 1
        max_money += 5
    else:
        print("Oh that's too bad, I'll take your bet.")
        print("Balance: %s" % total_dollars)
        total_rounds += 1
        print("You've run out of money, you lasted %s rounds." % total_rounds)

    # When you should have stopped

# print("You should have stopped at round %s." % best_round)
# print("You had %s dollars that round" % max_money)
