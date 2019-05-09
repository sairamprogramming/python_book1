# This program has a recursive function.

def main():
    print('This is a recursive function.')
    message()

def message():
    print('This is a recursive function.')    
    message()

# Call the main function.
main()    