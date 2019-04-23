# Distance Travelled.

# Getting speed from the user.
speed = float(input("What is the speed of the vehicle in mph? "))

# Input validation for speed variable.
while speed < 0:
    print("ERROR! speed cannot be a negative number.")
    speed = float(input("What is the speed of the vehicle in mph? "))

# Getting time from the user.
time = int(input('How many hours has it travelled? '))

# Input validation for time variable.
while time < 0:
    print("ERROR! time cannot be a negative number.")
    time = int(input('How many hours has it travelled? '))

# Displaying Heading
print("Hours\tDistance")
print('---------------')

# Calculating distance for each hour.
for hour in range(1, time + 1):
    distance = speed * hour
    # Printing the hour and distance.
    print(hour, '\t', distance)