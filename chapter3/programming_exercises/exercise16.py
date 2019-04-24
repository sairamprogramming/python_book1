# February Days

# Getting year input from the user.
year = int(input("Enter year: "))

# Checking if the given year is a leap year.
if (year % 4 == 0 and year != 0) or (year % 400 == 0):
    february_days = 29
else:
    february_days = 28

# Displaying the output (number of day in feburary).
print("In", year, "February has", february_days, "days.")