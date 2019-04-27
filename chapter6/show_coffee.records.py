# This program displays the records in the
# coffee.txt file.
def main():
    # Open the coffee.txt file.
    coffee_file = open('coffee.txt', 'r')

    # read the first record's description field.
    descr = coffee_file.readline()

    # read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float(coffee_file.readline())

        # Strinp the '\n' from the description.
        descr = descr.rstrip('\n')
        
        # Display the record.
        print('Description:', descr)
        print('Quantity:', qty)

        # Read the next description.
        descr = coffee_file.readline()
    
    # Close the file.
    coffee_file.close()

# Call the main function.
main()