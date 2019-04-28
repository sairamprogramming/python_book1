# File Head Display.

def main():
    # Get the filename from the user.
    filename = input('Enter the filename: ')

    # Handle Exceptions
    try:
        # Open the file given by the user.
        if filename[-3:] == 'txt':
            infile = open(filename, 'r')
        else:
            infile = open(filename + '.txt', 'r')
        
        # Initalize count (need to read only 5 lines or less)
        count = 5

        # Read the first line(to activate the while loop).
        line = infile.readline()

        # Print the lines from the file.
        while line != '' and count > 0:
            line = line.rstrip('\n')
            print(line)
            # Decrement count by 1.
            count -= 1
            # Read lines from the file
            line = infile.readline()
        
        # Close the file.
        infile.close()
        print('The File has been displayed.')
    except FileNotFoundError:
        print('Error! the file is not found.')

# Call the main function.
main()