# This program saves a list of numbers to a file.

def main():
    # Create a list of numbers.
    numbers = list(range(1,7 + 1))

    # Open the file for writing.
    outfile = open('numberlist.txt', 'w')

    # Write the list to the file.
    for item in numbers:
        outfile.write(str(item) + '\n')
        
    # Close the file.
    outfile.close()

# Call the main file.
main()