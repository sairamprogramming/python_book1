# Program to find the number of frequencies 

import random

def main():
    # Dictionary to hold the number frequencies.
    number_frequencies = {}

    # Adding the occurance of random number to dictionary.
    for unsed_variable in range(100):
        # Creating a random number in range 1 to 10 inclusive.
        random_number = random.randint(1,10)

        if random_number not in number_frequencies:
            number_frequencies[random_number] = 0

        number_frequencies[random_number] += 1

    # Sorting the key values to get print in order.
    keys = list(number_frequencies.keys())
    keys.sort()

    # Printing the number frequencies.
    print("Printing the random number frequencies:")
    for key in keys:
        print("%.2d" % key +": " + str(number_frequencies[key]))

# Calling the main function.
main()               