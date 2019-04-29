# Program to count lowercase characters in a string.

def main():
    my_string = input('Enter a string: ')

    lower_count = 0

    for ch in my_string:
        if ch.islower():
            lower_count += 1

    print('The number of alphanumberic chracters are', lower_count)

main()
