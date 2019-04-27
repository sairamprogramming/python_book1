# This program reads and displays the contents
# of the philosophers.txt file.

def main():
    # Open a file named philosophers.txt .
    inline = open('philosophers.txt', 'r')

    # Read the file's content.
    file_contents = inline.read()

    # Close the file.
    inline.close()

    # Print the data that was read into memory.
    print(file_contents)

# Call the main function.
main()