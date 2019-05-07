# This program assigns random numbers to 
# a two-dimensional list.
import random

# Constants for rows and columns.
ROWS = 3
COLUMNS = 4

def main():
    # Create a two-dimensional list.
    values = [[0]*4, [0]*4, [0]*4]
    
    # Fill the list with random numbers.
    for r in range(ROWS):
        for c in range(COLUMNS):
            values[r][c] = random.randint(1, 100)
    
    # Display the values.
    print(values)

# Call the main function.
main()