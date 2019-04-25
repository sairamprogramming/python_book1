# Prime Numbers.

# Defining the main function.
def main():
    # Getting input from the number.
    number = int(input("Enter a number: "))

    # Display output.
    if is_prime(number):
        print("Given number is prime.")
    else:
        print("Given number is not prime.")

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