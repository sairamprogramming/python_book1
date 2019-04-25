# Maximum of Two Values.

# Defining the main function.
def main():
    # Getting 2 values from the user.
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    # Printing the maximum of the two values.
    print(max(a,b))

# This function returns the greater of the two.
def max(a,b):
    if a > b:
        return a
    return b

# Calling the main function.
main()