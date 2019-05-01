# Name Search.

# This program displays if a name is popular for boys and girls.

def main():
    # Opening the files in read mode.
    boyfile = open('BoyNames.txt', 'r')

    girlfile = open('GirlNames.txt', 'r')

    # Initalzing lists that hold the names.
    boy_names = []
    girl_names = []

    # Entering the names in the lists.
    # Using .lower() method to compare ignoring captial letters.
    name  = boyfile.readline()
    
    while name != '':
        name = name.rstrip('\n')
        boy_names.append(name.lower())
        name = boyfile.readline()
    
    name = girlfile.readline()
    
    while name != '':
        name = name.rstrip('\n')
        girl_names.append(name.lower())
        name = girlfile.readline()
    
    # Closing the files.
    boyfile.close()
    girlfile.close()

    # Getting name to search from the user.
    search_name = input("Enter name to search: ")
    search_name = search_name.lower()

    # Condition on if given name is popular amoung boys and girls.
    if search_name in boy_names and search_name in girl_names:
        print(search_name, "is popular for boys and girls.")
    elif search_name in boy_names:
        print(search_name, "is popular for boys.")
    elif search_name in girl_names:
        print(search_name, "is popular for girls.")
    else:
        print(search_name, "is not popular amoung boys and girls.")

# Calling the main function.
main()