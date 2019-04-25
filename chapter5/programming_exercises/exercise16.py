# Odd/Even Counter.
import random

# Defining the main function.
def main():
    # Initalizing the counter variables for even and odd integers.
    count_even = 0
    count_odd = 0

    # Counting all the even and odd numbers from a sequence of random integers.
    for i in range(100):
        number = random.randint(1,1000)

        if is_even(number):
            count_even += 1
        else:
            count_odd += 1
    
    # Display the output.
    print("Total even numbers:", count_even)
    print("Total odd numbers:", count_odd)

# Function returns True is number is even, else returns False
def is_even(number):
    return number % 2

# Calling the main function.
main()
            