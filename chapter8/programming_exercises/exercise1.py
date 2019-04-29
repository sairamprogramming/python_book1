# Program on strings.

def main():
    first = input('Enter first names: ')
    last = input('Enter last name: ')

    try:
        # Display initials.
        print(first[0].upper() + "." + last[0].upper())

        # Dispay name in address book.
        print(first + " " + last.upper())

        # Display username.
        print(first[0].lower() + last.lower())
    except Exception as err:
        print(err)

main()