# Quater of the year.

# Get month from the user.
month = int(input("Enter the month(between 1 and 12):"))

# Check which quarter the month lies in.
if month >= 1 and month <= 12:
    if month <= 3:
        print("First Quarter.")
    elif month <= 6:
        print("Second Quareter.")
    elif month <= 9:
        print("Third Quarter.")
    else:
        print("Fourth Quarter.")
else:
    print("You have not entered a valid input for month.")