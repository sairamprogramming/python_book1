# This program writes three lines of data
# to the file.

def main():
    # Open a file name philosophers.txt .
    outfile = open('philosophers.txt', 'w')

    # Write names of three philosophers
    # to the file.
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Bruke\n')
    
    # Close the file
    outfile.close()

# Call the main function.
main()