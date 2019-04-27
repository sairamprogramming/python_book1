# This program writes items to a file.

def main():
    # Opening a file.
    outfile = open('things.txt', 'w')

    # Writing data to a file.
    outfile.write('Tiger\n')
    outfile.write('Mango\n')
    outfile.write('India\n')
    
    # closing connection to the file object.
    outfile.close()

    print('Items Added to things.txt')

# Call the main function.
main()