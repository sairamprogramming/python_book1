# File Display.
# Program to print all the contents in numbers.txt file.

def main():
    # Opening file in read mode
    infile = open('numbers.txt', 'r')

    # Inital read of file (reading first line)
    number = infile.readline()

    # Reading all the lines and printing it.
    while number != '':
        # Removing the extra '\n' from number string
        number = number.rstrip('\n')
        print(number)
        number = infile.readline()
    
    # Closing the file.
    infile.close()
    print('Displayed all contents of numbers.txt')

# Calling the main function.
main()