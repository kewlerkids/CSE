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
