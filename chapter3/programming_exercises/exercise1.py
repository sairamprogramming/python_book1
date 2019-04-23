# Number Analyser.

# Getting the integer from the user.
number = int(input("Enter an integer: "))

# Displaying if the integer is +ve, -ve or 0.
if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
else:
    print("Negative")

# Check if number is odd or even.
if number % 2 == 0:
    print("Even")
else:
    print("Odd")