# Program to get unique words from the text file 'text.txt'

def main():
    infile = open('text.txt', 'r')

    text = infile.read()
    # Creating a list of all words.
    text = text.split()

    infile.close()

    # Getting unique words from the text in text.txt file.
    unique_words = set(text)

    # Printing all the unique words.
    print(unique_words)

# Calling the main function.
main()    