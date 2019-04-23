# Bug Collector

# Accumulator for total bugs collected
total_bugs_collected = 0

# Bug collector, collects for 5 days.
for day in range(5):
    # Getting input from the user for bug collected on the day.
    bug_collected_today = int(input("How many bugs have you collected today? "))

    while bug_collected_today < 0:
        print("ERROR! cannot be a negative number.")
        bug_collected_today = int(input("How many bugs have you collected today? "))
    
    total_bugs_collected += bug_collected_today

# Display the total number of bugs collected.
print("The total number of bugs collected is", total_bugs_collected)