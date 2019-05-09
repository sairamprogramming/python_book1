# Design a recursive function that accepts an integer argument, n , and prints every second
# number from n down to a minimum of 0. Assume that n is always a positive integer.

# Main function.
def main():
    number = int(input("Enter number: "))

    print_number(number)

# The recursive function.
def print_number(n):
    # Base Case
    if n == -1:
        return 
    # Recursive Case        
    else:
        print(n)
        print_number(n - 1)    

# Calling the main function.
main()        