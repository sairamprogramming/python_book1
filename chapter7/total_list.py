# This program calculates the total values 
# in a list.

def main():
    # Create a list.
    numbers = [2, 4, 6, 8, 10]

    # Create a variable to use as an accumulator.
    total = 0

    # Calculate the total of the list of elements.
    for value in numbers:
        total += value
    
    # Display the total of the list of elements.
    print('The total of the elements is', total)

# Call the main function.
main()