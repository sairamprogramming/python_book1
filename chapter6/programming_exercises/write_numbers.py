# Program to create and write numbers 1 to 100 to numbers.txt file.
# Not part of any exercise just to create a file for testing all the exercise programs.

def main():
    # Opening the file in write mode
    outfile = open('numbers.txt', 'w')

    # Writing numbers 1 to 100 to the file.
    for number in range(1, 100 + 1):
        outfile.write(str(number) + '\n')
    
    # Closing the file.
    outfile.close()
    print('Written numbers to numbers.txt file.')

# Calling the main function.
main()