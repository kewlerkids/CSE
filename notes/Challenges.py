import random


def challenge1(name1, name2):
    print("%s, %s" % (name2, name1))


challenge1("Aile", "Banuelos")


def challenge3(base, height):
    print(base*height/2)


challenge3(10, 5)


def challenge4(number):
    if number == 0:
        return "This number is zero"
    if number > 0:
        return "This number is positive"
    if number < 0:
        return "This number is negative"


print(challenge4(random.randint(-10, 10)))


def challenge7(number):
    print(number+number*number+number**3)


challenge7(2)


def challenge8(number):
    if number >= 2000:
        return "It is between 150 and 2000"

    elif number >= 150:
        return "It is between 150 and 2000"

    elif number < 2000:
        return "Not between given range"

    elif number < 150:
        return "Not between given range"


print(challenge8(random.randint(0, 3000)))
