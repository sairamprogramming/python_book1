# Sentence Capitalizer

# Program to captilze the first letter in a sentence in a given string.

def main():
    # Getting string input from the user.
    string_input = input("Enter string: ")

    # Displaying the original string and string with captialized sentences.
    print("Given sentence:", string_input)
    print("Captilized sentences:", sentence_captalize(string_input))

# This function takes a string input and captalizes the sentences in the
# string and returns it.
def sentence_captalize(sentence):
    sentence = sentence.split('. ')

    for index in range(len(sentence)):
        if sentence[index][0].islower():
            sentence[index] = sentence[index][0].upper() + sentence[index][1:]
    
    return '. '.join(sentence)

# Calling the main function.
main()