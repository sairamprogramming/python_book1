# Program to count alphanumeric characters in a string.

def main():
    my_string = input('Enter a string: ')

    alnum_count = 0

    for ch in my_string:
        if ch.isalnum():
            alnum_count += 1

    print('The number of alphanumberic chracters are', alnum_count)

main()
