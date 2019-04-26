# Popilation

# Getting the number of starting organisms from the user.
starting_organisms = int(input("Enter the starting number of organisms: "))

# Input Validation.
while starting_organisms < 0:
    print("Invalid Input, the number of starting organisms cannot be negative.")
    starting_organisms = int(input("Enter the starting number of organisms: "))

# Getting the average daily increase in the population in percentage.
average_daily_increase = float(input('Enter the average daily population increase(in percentage): '))

# Input Validation.
while average_daily_increase < 0:
    print("Invalid Input, the average daily population cannot be negative.")
    average_daily_increase = float(input('Enter the average daily population increase(in percentage): '))

# Reducing the percentage to decimal (in range 0 to 1)
average_daily_increase = average_daily_increase / 100

# Getting the number of days for which we have to calculate for.
number_of_days = int(input('Enter the number of days of the study: '))

# Input Valdiation.
while number_of_days < 0:
    print("Invaild Input, the number of days cannot be negative.")
    number_of_days = int(input('Enter the number of days of the study: '))

# Printing the heading.
print("Day Approximate", end = '')
print("\t\tPopulation")

# Calculting the number of organisms increase for days 1 to number_of_days.
# Printing the output.
for day in range(1, number_of_days + 1):
    if day == 1:
        number_of_organisms = starting_organisms
    else:
        number_of_organisms += number_of_organisms * average_daily_increase
    print(day, '\t\t', number_of_organisms)


