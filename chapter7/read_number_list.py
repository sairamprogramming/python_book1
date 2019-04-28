# This program reads numbers from a file into a list.

def main():
    # Open the file for reading.
    infile = open('numberlist.txt', 'r')

    # Read the contents of the file into a list.
    numbers = infile.readlines()

    # Close the file.
    infile.close()

    # Convert each element to int.
    index = 0
    while index < len(numbers):
        numbers[index] = int(numbers[index])
        index += 1
    
    # Print the numbers.
    print(numbers)

# Call the main function.
main()