# Program to convert all lowercase 't' to uppercase.

def main():
    my_string = input('Enter a string: ')

    # More complicated implementation. Using slicing and concatenation.
    for index in range(len(my_string)):
        if my_string[index] == 't' and index != len(my_string) + 1:
            my_string = my_string[:index] + "T" + my_string[index+1:]
        elif my_string[index] == 't' and index != len(my_string) + 1:
            my_string = my_string[:index] + 'T'
    
    print(my_string)

main()