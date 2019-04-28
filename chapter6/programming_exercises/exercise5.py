# Sum of numbers.

def main():
    # Open the file.
    infile = open('numbers.txt', 'r')

    # Initalize the total accumulator.
    total = 0

    # Read all the numbers in the file.
    for number in infile:
        # Sum all the numbers.
        number = int(number)
        total += number
    
    # Close the file and print total.
    infile.close()
    print('Total of numbers:', total)

# Call the main function.
main()