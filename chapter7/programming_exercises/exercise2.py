# Lottery Number Generator.

# Program to generate a 7 digit lottery number.
import random

# Constant holds the length of the lottery number.
LOTTERY_NUMBER_LENGTH = 7

def main():

    # Generating the lottery number.
    lottery_numbers = []

    # temp is unsed placeholder variable. (Has no use in this program)
    for temp in range(LOTTERY_NUMBER_LENGTH):
        lottery_numbers.append(random.randint(0, 9))

    # Disply the lottery number.
    print('Lottery Number ', end = '')

    for number in lottery_numbers:
        print(number, end='')
    
    print()

# Calling the main function.
main()