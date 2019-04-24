# This program demonstrates passing two strings as 
# keywords to a function.

def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Your name is reversed is')
    reverse_name(last=last_name, first=first_name)

def reverse_name(first, last):
    print(last, first)

# Call the main function.
main()