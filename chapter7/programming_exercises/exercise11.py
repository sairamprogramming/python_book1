# Lo Shu Magic Square.

# This program finds if a given square matrix is lo shu square matrix.

# Constant to hold the number of rows and columns in the matrix
ROWS = 3
COlUMNS = 3

def main():
    # Iniatilzing the square matrix
    matrix = []

    # Getting values to square matrix
    print("Enter numbers in the range 1 to 9.")
    for row in range(ROWS):
        temp_list = []
        for column in range(COlUMNS):
            incorrect_input = True
            number = 0
            # This method is to get the right value in the appropriate position in the matrix.
            while incorrect_input:
                try:
                    number = float(input("Enter the element value at position(" 
                                            + str(row + 1) + ", " + str(column + 1) + "): "))

                    if number < 1 or number > 9:
                        print("Enter numbers in the range 1 to 9.")
                        continue

                    incorrect_input = False
                except ValueError:
                    print("Error, Enter Valid Numbers!")
            

            temp_list.append(number)
        
        matrix.append(temp_list)

    # Printing the matrix to display.
    print_matrix(matrix)

    # Getting the value of sum of first row of matrix
    # and setting it as checking condition for all 
    # other sums of rows, columns and diagonals.
    sum_to_check = total(matrix[0])
    
    # is_true variable holds the boolean for if
    # given matrix is lo shu square matrix. 
    is_true = True

    # Checking all rows in the matrix.
    row_index = 0

    while row_index < ROWS and is_true:
        if sum_to_check != total(matrix[row_index]):
            is_true = False
            break
        row_index += 1
    
    # Checking all columns in the matrix.
    column_index = 0

    while column_index < COlUMNS and is_true:
        column_list = get_column(matrix, column_index)
        
        if sum_to_check != total(column_list):
            is_true = False
            break
        
        column_index += 1

    # Checking the diagonals of the matrix.
    if is_true:
        diagonal_list = get_diagonal1(matrix)

        if total(diagonal_list) != sum_to_check:
            is_true = False
        
        diagonal_list = get_diagonal2(matrix)

        if total(diagonal_list) != sum_to_check:
            is_true = False                     
    
    # Printing if the given matrix is lo shu square matrix or not.
    if is_true:
        print("Given Matrix is Lo Shu Square Matrix.")
    else:
        print("Given Matrix is not Lo Shu Square Matrix.")

# Function prints a given matrix to screen.
def print_matrix(matrix):
    for row in range(ROWS):
        for column in range(COlUMNS):
            print(matrix[row][column], end=" ")
        print()

# Function returns a list of 1st diagonal elements 
# in the matrix.
def get_diagonal1(matrix):
    result_list = []

    for index in range(len(matrix)):
        result_list.append(matrix[index][index])
    
    return result_list

# Function returns a list of 2nd diagonal elements
# in the matrix.
def get_diagonal2(matrix):
    result_list = []

    for index in range(len(matrix)):
        result_list.append(matrix[len(matrix) - (index + 1)][index])
    
    return result_list

# Function returns a list of all column elme
def get_column(matrix, column_index):
    result_list = []

    for row_index in range(len(matrix)):
        result_list.append(matrix[row_index][column_index])

    return result_list  
    

# Function returns the sum of all elements in the list.
def total(given_list):
    total = 0.0

    for number in given_list:
        total += number

    return total

# Calling the main function.
main()