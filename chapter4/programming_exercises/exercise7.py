# Pennies for pay

# Getting the number of days to calculate the salary for from the user.
number_of_days = int(input("Enter the number of days: "))

# Input Validation
while number_of_days < 0:
    print("Invalid Input, number of days cannot be negative.")
    number_of_days = int(input("Enter the number of days: "))

# Condition if input number of days is 0.
if number_of_days == 0:
    total_salary_pennies = 0
else:
    # Initalizing the first day salary
    total_salary_pennies = 1

    # Calculating the salary for the remaining days given as input by the user
    for the_day in range(2, number_of_days + 1):
        total_salary_pennies *= 2

# Converting the salary in pennies to dollars
total_salary_dollars = total_salary_pennies / 100

# Displaying the output.
print("The total salary is $", format(total_salary_dollars, ',.2f'), sep = '')