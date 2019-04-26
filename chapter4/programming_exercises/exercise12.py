# Calculating the factorial of a number.

# Getting number to find the factorial for from the user.
number = int(input('Enter the number to calculate the factorial(non-negative number): '))

# Input Validation. (Number cannot be negative)
while number < 0:
    print('Invalid Number, Enter a positive integer.')
    number = int(input('Enter the number to calculate the factorial(non-negative number): '))

# Initaling the factorial variable, multiplicative accumulator
factorial = 1

# Finding the factorial.
for i in range(1, number + 1):
    factorial *= i

# Display the output.
print("The factorial is", factorial)
