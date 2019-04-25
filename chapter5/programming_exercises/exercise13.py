# Falling Distance.

# contant holds the acceleration due to gravity.
GRAVITY = 9.8   # meters / (seconds ** 2)

# Defining the main function.
def main():
    # time is in seconds.
    for time in range(1,11):    # in seconds
        distance = falling_distance(time)   # in meters

        print("Distance travelled in", time, "seconds is", format(distance, '.4f'), "meters.")

# Function that finds the distance travelled by a falling object given the time.
def falling_distance(time):
    return 0.5 * GRAVITY * (time ** 2)

# Calling the main function.
main()