# Roulette Wheel Color

# Getting the pocket number from the user.
number = int(input("Enter the roulette number (1 to 36 inclusive): "))

# Finding the color of the pocket from the input number.
if number == 0:
    print('pocket is green.')
elif number <= 10:
    if number % 2 == 0:
        print('pocket is black.')
    else:
        print('pocket is red.')
elif number <= 18:
    if number % 2 == 0:
        print('pocket is red.')
    else:
        print("pocket is black.")
elif number <= 28:
    if number % 2 == 0:
        print('pocket is black.')
    else:
        print('pocket is red.')
elif number <= 36:
    if number % 2 == 0:
        print('pocket is red.')
    else:
        print('pocket is black.')
else:
    print('You have entered a invalid pocket number.')