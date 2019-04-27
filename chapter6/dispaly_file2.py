# This program displays the contents
# of a file.

def main():
    # Get the file name of a file.
    filename = input('Enter a filename: ')

    try:
        # Open the file.
        inflie = open(filename, 'r')

        # Read the files's contents.
        contents = inflie.read()

        # Display the file's contents.
        print(contents)

        # Close the file.
        inflie.close()
    except IOError:
        print("An error occured trying to read")
        print("the file", filename)

# Call the main function.
main()