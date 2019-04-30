# Character Analysis.

# This program reads a file and prints:
# Number of uppercase letters in the file.
# Number of lowercase letters in the file.
# Number of digits in the file.
# Number of whitespace characters in the file.

def main():
    # Open the file in read mode.
    infile = open('text.txt', 'r')

    file_content = infile.read()

    # Closing the file.
    infile.close()
    
    # Initazling variables.
    uppercase_number = 0
    lowercase_number = 0
    digit_number = 0
    whitespace_number = 0

    # Finding the total of all the required variables respectively.
    for character in file_content:
        if character.isupper():
            uppercase_number += 1
        elif character.islower():
            lowercase_number += 1
        elif character.isdigit():
            digit_number += 1
        elif character.isspace():
            whitespace_number += 1
    
    # Display the output.
    print("Total uppercase characters:", uppercase_number)
    print("Total lowercase characters:", lowercase_number)
    print("Total digits:", digit_number)
    print("Total whitespace:", whitespace_number)

# Call the main function.
main()