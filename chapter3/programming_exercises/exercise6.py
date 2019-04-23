# Magic Dates.
# if month * day == last two digits of the year, then the date is magic date.

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year_last2_digits = int(input("Enter the last two digits of the year: "))

if day * month == year_last2_digits:
    print("Given date is a magic date.")
else:
    print("Given date is not a magic number.")