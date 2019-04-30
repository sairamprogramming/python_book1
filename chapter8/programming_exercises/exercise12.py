# Pig Latin.

# This program converts a given sentence into pig latin
# using the method described in the exercise 12.

def main():
    # Getting input from the user.
    string_input = input("Enter sentence to convert: ")

    string_input = string_input.split()

    pig_latin_sentence = ''

    # Converting given sentence to pig latin.
    for word in string_input:
        temp_word = word[1:] + word[0] +'AY'
        pig_latin_sentence += temp_word + " "
    
    # Display the output.
    print(pig_latin_sentence)  

# Call the main function.
main()