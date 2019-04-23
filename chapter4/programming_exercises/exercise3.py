# Lap Times

# Getting total number of laps run from the user.
number_of_laps = int(input('Enter the total number of laps: '))

# Input validation for 'number_of_laps' variable.
while number_of_laps < 0:
    print("ERROR! cannot be a negative number.")
    number_of_laps = int(input('Enter the total number of laps: '))

# Accumulator for time of all laps
total_time = 0.0

# Finding the total time, fastest time and slowest time of all laps.
for lap in range(number_of_laps):
    # Getting current lap time from the user
    lap_time = float(input("Time taken for lap " + str(lap + 1) + ": "))

    # Input validation for 'lap_time' variable.
    while lap_time < 0:
        print("ERROR! cannot be a negative number.")
        lap_time = float(input("Time taken for lap " + str(lap + 1) + ": "))
    
    if lap == 0:
        # Initalizing fastes and slowest time of each lap
        fastest_time = lap_time
        slowest_time = lap_time

    if lap_time < fastest_time:
        fastest_time = lap_time
    
    if lap_time > slowest_time:
        slowest_time = lap_time
    
    total_time += lap_time

# Calculating the average lap time.
average_lap_time = total_time / number_of_laps

# Displaying the fastest, slowest and average time.
print("Fastest time:", format(fastest_time, '.3f'))
print("Slowest time:", format(slowest_time, '.3f'))
print('Average time:', format(average_lap_time, '.3f'))
    