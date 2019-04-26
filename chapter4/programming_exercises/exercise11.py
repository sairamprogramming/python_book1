# Sleep Debt

# Constant holds the desirable sleep per day
SLEEP_DESIRABLE_AMOUNT_PER_DAY = 8
# The constant is the start of the week
START_WEEK = 1
# Constant represents the end of the week
END_WEEK = 7

# Initalizing the accumulator to count the total amount of sleep of a week
total_amount_sleep = 0

# Need to calculate for 7 days of the week
for day in range(START_WEEK, END_WEEK + 1):
    # Getting the amount of sleep in hours per day.
    number_hours_sleep = float(input("Enter the amount of sleep you had on " + str(day) + " : "))

    # Input Validation.
    while number_hours_sleep < 0:
        print("Invalid Input, number of hours of sleep cannot be negative.")
        number_hours_sleep = float(input("Enter the amount of sleep you had on " + str(day) + " : "))

    total_amount_sleep += number_hours_sleep

# Calculating the sleep debt
sleep_debt = (SLEEP_DESIRABLE_AMOUNT_PER_DAY * END_WEEK) - total_amount_sleep

# Printing the output.
print('Sleep Debt:', sleep_debt)

if sleep_debt <= 0:
    print("You got good sleep this week!")
