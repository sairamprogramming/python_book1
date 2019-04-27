# This program reads items line by line from a file.

def main():
    # Opening a file in read mode.
    infile = open('things.txt', 'r')

    # Reading file line by line and printing it.
    for line in infile:
        # Removing the extra '\n'.
        line = line.rstrip('\n')
        print(line)
    
    # Closing the file.
    infile.close()

    print('Have dispayed all the contents in the file things.txt')

# Call the main function.
main()