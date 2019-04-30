# Vowels and Consonants.

# This tuple holds list of vowel characters in the alphabets.
VOWELS = ('a','e','i','o','u')

# This function takes a string input and returns the number of
# vowels in the string. 
def total_vowels(string):
    number_vowels = 0 

    for character in string:
        if character.lower() in VOWELS:
            number_vowels  += 1
    
    return number_vowels

# This function takes a string and returns the number of
# consonants in the string.
def total_consonants(string):
    number_consonants = 0

    for character in string:
        # First condition is required, since consonants are only alphabets.
        if character.isalpha() and (character.lower() not in VOWELS):
            number_consonants += 1
    
    return number_consonants

def main():
    # Get string input from the user.
    string_input = input("Enter a string: ")

    # Display the total number of vowels and consonants in the input string.
    print("Total vowels in the string is", total_vowels(string_input))
    print("Total consonants in the string is", total_consonants(string_input))

# Call the main function.
main()