# Function to print a string backwards.

def main():
    my_string = input('Enter a string: ')

    print(string_reverse(my_string))

# Function reverses given string argument and returns the result back to the calling function.
def string_reverse(string):
    temp_string = ''

    for index in range(-1, -len(string)-1, -1):
        temp_string += string[index]
    
    return temp_string

# Call the main function.
main()