# This program displays five random
# numbers in the range of 1 to 100.
import random

def main():
    for count in range(5):
        # Get a random number
        print(random.randint(1, 100))

# Call the main function.
main()