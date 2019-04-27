# This program reads numbers from a file.

def main():
    # Opening file in read mode.
    infile = open('numbers_list.txt', 'r')

    # Reading numbers from the file( Numbers are in string format.)
    for number in infile:
        # Removing the extra '\n' from the number string.
        number = number.rstrip('\n')
        print(number)
    
    # Closing the file.
    infile.close()
    print('Displayed all the items in the file numbers_list.txt')

# Calling the main function.
main()