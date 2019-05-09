# Design a function that uses recursion to raise a number to a power. The function should
# accept two arguments: the number to be raised, and the exponent. Assume the exponent is
# a nonnegative integer.

# The main function.
def main():
    number = int(input('Enter number: '))
    power = int(input('Enter number: '))

    print(to_power(number, power))

# The recurisive case.
def to_power(n, p):   
    # Base Case. 
    if p == 0:
        return 1
    # Recursive Case.
    else:
        return n * to_power(n,p-1)

# Calling the main function.
main()    