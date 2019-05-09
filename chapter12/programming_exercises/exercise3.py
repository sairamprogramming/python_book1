# Write a recursive function that accepts an integer argument, n . The function should display
# n lines of asterisks on the screen, with the first line showing 1 asterisk, the second line
# showing 2 asterisks, up to the n th line which shows n asterisks.

# Main function
def main():
    n = int(input("Enter n: "))
    # Need n_hold since we need to know the value of n in every recursive case.
    n_hold = n
    lines(n - 1, n_hold)

# Recursive function.
def lines(n, n_hold):
    # Base Case.
    if n == -1:
        return
    # Recursive Case.
    else:
        print('*' * (n_hold - n))
        lines(n - 1, n_hold)    

# Calling the main function.
main()        