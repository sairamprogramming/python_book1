# This program displays the contents
# of a file.

def main():
    # Get the file name of a file.
    filename = input('Enter a filename: ')

    # Open the file.
    
    inflie = open(filename, 'r')

    # Read the files's contents.
    contents = inflie.read()

    # Display the file's contents.
    print(contents)

    # Close the file.
    inflie.close()

# Call the main function.
main()