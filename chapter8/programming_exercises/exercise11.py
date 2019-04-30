# Word Seperator.

# This program takes a camelcase sentence as input and
# converts the string and prints the result.

def main():
    # Getting camelcase sentence from the user.
    string_input = input("Enter camelcase sentence: ")

    # Initalizing the variable that holds the result.
    result_string = string_input[0]
    
    # Covnerting the camelcase  sentence to regular sentence.
    for index in range(1, len(string_input)):
        if string_input[index].isupper():
            result_string += " " + string_input[index].lower()
        else:
            result_string += string_input[index]

    # Display the result.
    print(result_string)    

# Call the main function.
main()