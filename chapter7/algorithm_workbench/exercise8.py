# Program to create a 5 x 3 matrix by using user input.

ROW = 5
COLUMN = 3

def main():
    matrix = []

    for i in range(ROW):
        matrix.append([0] * COLUMN)
    
    # Getting inputs from the user.
    for r in range(ROW):
        for c in range(COLUMN):
            # This is to get valid number inputs from the user.
            # Exception handling.
            found = True

            while found:
                try:
                    matrix[r][c] = int(input('Enter a number: '))
                    found = False
                except ValueError:
                    print('Enter a valid number.')
    
    # Display the matrix.
    print(matrix)

# Calling the main function.
main()
            

