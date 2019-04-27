# This program reads all of the values in
# the sales.txt file.

def main():
    # Open the file.
    sales_file = open('sales.txt', 'r')

    # Read the first line from the file, but
    # don't need to convert to a number yet, We
    # still need to test for an empty string.
    line = sales_file.readline()

    # As long as an empty string is not returned
    # from the readLine, continue processing.
    while line != '':
        # Convert line to float.
        amount = float(line)

        # Format and display the amount.
        print(format(amount, '.2f'))

        # Read the next line.
        line = sales_file.readline()
    
    # Close the file.
    sales_file.close()

# Call the main function.
main()