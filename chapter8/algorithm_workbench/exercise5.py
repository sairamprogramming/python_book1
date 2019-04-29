# Program to check if the function starts with 'https'.

def main():
    my_string = input("Enter string: ")

    if my_string.startswith('https'):
        print(True)
    else:
        print(False)
    
main()