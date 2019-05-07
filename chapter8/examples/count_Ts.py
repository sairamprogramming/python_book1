# This program counts the number of times
#  the letter T (uppercase of lowercase) 
# appears in a string.

def main():
    # Create a variable to use the hold the count.
    # The variable must start with 0.
    count = 0

    # Get a string from the user.
    my_string = input('Enter a string: ')

    # Count the Ts.
    for ch in my_string:
        if ch == 'T' or ch == 't':
            count += 1
    
    # Print the result.
    print('The letter T appears', count, 'times.')

# Call the main function.
main()