# Calories Burned

# Named constant for calories burned per minute.
CALORIES_BURNED_PER_MINUTE = 4.2

# Calculating the total caloires burned
for minutes in range(10,31,5):
    total_calories_burned = CALORIES_BURNED_PER_MINUTE * minutes

    print("Calories burned after", minutes, "of running is", format(total_calories_burned, '.2f'))