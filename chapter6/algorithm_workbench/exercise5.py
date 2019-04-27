# The program reads numbers from the file and prints the total.

def main():
    # Opening the file in read mode.
    infile = open('numbers_list.txt', 'r')

    # Initalizing the accumulator to sum all numbers read from the file.
    total = 0

    # Summing all the numbers read from the file.
    for number in infile:
        number = number.rstrip('\n')
        # Converting str to float(numeric type)
        number = float(number)
        total += number
    
    # Closing the file.
    infile.close()
    print('The total of the numbers in the file numbers_list.txt is', total)

# Calling the main function.
main()