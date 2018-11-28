'''
print("Hello World")
print()
# This is a comment. I can write whatever I want
# Here and it wont do anything about it.
# It has no effect on the code.
print()   # This adds extra spaces on the terminal
print("This will print here. Notice the spacing.")

a = 4
b = 3
print(a+b)
print(a*5)
print(5-3)
print(6/5)   # Results in a float (with decimals)

print("Figure this out")
print(6//4)  # Results in a integer (Without decimals)
print(12//3)
print(9//4)

# MORE MATH STUFF
print("Figure this stuff out too...")
print(6 % 4)
print(5 % 3)
print(9 % 4)


# Variables
car_name = "The Wiebe mobile"
car_type = "Tesla"
car_cylinders = 1024
car_miles_per_gallon = 0.01

print("I have a car called %s. It's pretty nice." % car_name)

# Input
# name = input("What is your name? ")
# print("Hello %s" % name)

# Auto-comment - Ctrl + /
# age = input("How old are you? ")
# print("%s?! You belong in a museum." % age)

# Hidden age
real_age = int(input("How old are you? >_"))
hidden_age = real_age + 5
print(hidden_age)
print("&d is incredibly old." % hidden_age)
'''

# functions
def printHelloWorld():
    print("Hello World!")


printHelloWorld()
'''
This is a multi-line comment
I can type anywhere here.
'''


# f(x) = 2x + 3
def f(x):
    print(2*x + 3)


f(1)
f(5)
f(5000)

#loops
for i in (1,2,3):
    printHelloWorld()

    print()
for i in range(10):
    printHelloWorld()

    print()
for i in range(5):   # Range starts at 0 and goes to 4
    f(i)

for i in range(5):
    print(i**2)


# while loops
a = 0
while a < 10:
    print(a)
    a += 1  # This is the same thing as a = a + 1

'''
Hints with loops:
For loops - use when you know EXACTLY how many iterations
While loops - Use when you DON'T know how many iterations
'''

# Random numbers
import random  # This should always be on line 1
print(random.randint(0, 100))


# Control Statements
def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


print(grade_calc(76))

# Equality Statements
print(5 > 3)
print(5 >= 3)
print(5 == 3)

'''
a = 3 # A is set to 3
a == 3 # Is A equal to 3?
'''

# Lists
shopping_list = ["Whole Milk", "PC", "Eggs", "Trash (Xbox One)", "Other Trash(PS4)"]
print(shopping_list)
print(shopping_list[0])
print("The second thing in the list is %s" % shopping_list[1])
print("The length of the list is %d" % len(shopping_list))

# Changing Elements in a list
shopping_list[0] = "2% milk"
print(shopping_list)
print(shopping_list[0])

# Looping through lists
for item in shopping_list:
    print(item)

'''
1.Make a list
2.Change the third thing in the list
3.Print the item
4.Print the full list
'''
food = ["Eggs", "Cheese", "Pistachio", "Raspberries"]
food[2] = "Apples"
print("The last thing in the list is %s" % food[len(food) - 1])
print(food)

# Getting part of a list
print(food[1:3])
print(food[1:4])
print(food[1:])
print(food[:2])

# Adding things to a list
christmas_list = []   # ALWAYS USE SQUARE BRACKETS
christmas_list.append("Tacos")
christmas_list.append("Bumblebee")
christmas_list.append("Red Dead Redemption 2")
print(christmas_list)
# Notice this is "object.method(Parameters)"

# Removing things from a list
christmas_list.remove("Tacos")
print(christmas_list)

'''
1.Make a new list with 3 items
2.Add a 4th item to the list
3.Remove one of the first three items from the list
'''

# Also removing things from a list
christmas_list.pop(0) # Removes the thing in the 0 index
print(christmas_list)

# Tuple
brands = ("Apple", "Samsung", "HTC")    # notice the parentheses


colors = ['Blue', 'Cyan', 'Teal', 'Red', 'Green', 'Orange', 'Purple',
          'Pink', 'Black', 'Gold', 'Magenta', 'Brown', 'Turquoise', 'White', 'Gray', 'Yellow']
print(len(colors))

# Find the index
print(colors.index("Gold"))

# Changing things into a list
string1 = "Turquoise"
list1 = list(string1)
print(list1)

for character in list1:
    if character == "u":
        # Replace with a *
        current_index = list1.index(character)
        list1.pop(current_index)
        list1.insert(current_index, "*")
        
# Changing lists into a string
print("".join(list1))

