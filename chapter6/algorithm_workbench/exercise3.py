# Program to write numbers to a file.

def main():
    # Opening the file in write mode
    outfile = open('numbers_list.txt', 'w')

    # Wrting numbers 1 to 100 to the file
    for i in range(1, 101):
        outfile.write(str(i) + '\n')
    
    # Closing the file.
    outfile.close()

    print('All data added to file numbers_list.txt')

# Calling the main function.
main()