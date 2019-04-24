# Defination of main function.
def main():
    get_name()
    print('Hello', name)            # <--- This causes an error (Since function is trying to access variable
                                    #       it cannot see 'name').

# Defination of get_name function
def get_name():
    name = input('Enter your name: ')

# Call the main function.
main()
