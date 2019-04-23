# Roman Numerals
# Program to show number between 1 to 10 in roman format.

number = int(input("Enter number: "))

if number >= 1 and number <= 10:
    if number == 1:
        print("I")
    elif number == 2:
        print("II")
    elif number == 3:
        print("III")
    elif number == 4:
        print("IV")
    elif number == 5:
        print("V")
    elif number == 6:
        print("VI")
    elif number == 7:
        print("VII")
    elif number == 8:
        print("VIII")
    elif number == 9:
        print("IX")
    elif number == 10:
        print("X")
else:
    print("You have not entered a valid input.")