# Prime Number List.

# Defining the main function.
def main():
    
    # Printing primes numbers in range 1 to 100.
    for number in range(1,101):
        if is_prime(number):
            print(number, end = " ")
    
    print()

# Function returns a boolean on if a number is prime.
def is_prime(number):

    # Eliminate all even numbers.
    if number % 2 == 0:
        return False

    for i  in range(3, number, 2):
        if number % i == 0:
            return False
    
    return True

# Calling the main function.
main()    