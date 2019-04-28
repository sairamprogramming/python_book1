# Line numbers.

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
        
        line_number = 1

        line = infile.readline()

        while line != '':
            line = line.rstrip('\n')
            print(str(line_number) + ':', line)
            line_number += 1
            line = infile.readline()
        
        infile.close()
        print('Displayed all contents in the file')
    except FileNotFoundError:
        print('Error, File not found.')

main()