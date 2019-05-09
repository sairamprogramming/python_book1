# Design a recursive function that accepts two arguments into the parameters x and y . The
# function should return the value of x times y . Remember, multiplication can be performed
# as repeated addition as follows:
# 7 3 4 5 4 1 4 1 4 1 4 1 4 1 4 1 4
# (To keep the function simple, assume x and y will always hold positive nonzero integers.)

# Main function
def main():
    # Getting the input from the user.
    x = int(input('Enter number x: '))
    y = int(input('Enter number y: '))

    print(multiply(x,y))

# Recursive function
def multiply(x, y):
    # Base Case
    if x == 1:
        return y
    # Recursive Case        
    else:
        return y + multiply(x - 1,y)    

# Call the main function.
main()        