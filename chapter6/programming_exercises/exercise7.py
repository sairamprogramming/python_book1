# Word List File Writer.

def main():
    # Getting the number of words to write to file from the user.
    number_words = int(input('Enter the number of words to enter the file: '))

    # Opening the file. In write mode.
    outfile = open('word_list.txt', 'w')

    # Getting the word from the user and writing it to file.
    for word_number in range(number_words):
        word = input("Enter word " + str(word_number + 1) + ": ")
        outfile.write(word + '\n')
    
    # Closing the file.
    outfile.close()
    print('The file has been updated.')

# Call the main function.
main()