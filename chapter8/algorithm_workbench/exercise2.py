# Program to count spaces in a string.

def main():
    my_string = input('Enter a string: ')

    space_count = 0

    for ch in my_string:
        if ch == ' ':
            space_count += 1

    print('The number of spaces are', space_count)

main()
