# This program uses recursion to find the GCD 
# of two numbers.

def main():
    # Get two numbers.
    num1 = int(input('Enter an integer: '))
    num2 = int(input('Enter another integer: '))

    # Display the GCD.
    if num1 >= num2:
        print('The greatest common divisor of')
        print('the two numbers is', gcd(num1, num2))
    else:        
        print('The greatest common divisor of')
        print('the two numbers is', gcd(num2, num1))
# The gcd function returns the greatest common
# divisor of two numbers.
def gcd(x,y):
    if x % y == 0:
        return y
    else:
        return gcd(x, x % y)    

# Call the main function.
main()        