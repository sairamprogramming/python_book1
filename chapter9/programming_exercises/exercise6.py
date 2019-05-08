# File Analysis

# This program performs file anaysis as shown below.

# It should display a list of all the unique words contained in both files.
# It should display a list of the words that appear in both files.
# It should display a list of the words that appear in the first file but not the second.
# It should display a list of the words that appear in the second file but not the first.
# It should display a list of the words that appear in either the first or second file, but not
# both.

def main():
    # Opening the files in read mode.
    infile = open('text.txt', 'r')
    file_input = open('text2.txt', 'r')

    # Getting unique words from the first file.
    unique_words = infile.read()
    unique_words = unique_words.split()
    unique_words = set(unique_words)

    # Getting unique words from the second file.
    unique_words2 = file_input.read()
    unique_words2 = unique_words2.split()
    unique_words2 = set(unique_words2)

    # Closing the file objects.
    infile.close()
    file_input.close()

    # Printing the output.
    print("Unique words that appear in first file.")
    print(unique_words)
    print()

    print("Unique words that appear in second file.")
    print(unique_words2)
    print()

    print("Displaying all words that appear in both the sets.")
    print(unique_words.union(unique_words2))
    print()

    print("Display words that appear only in first file.")
    print(unique_words.difference(unique_words2))
    print()

    print("Display words that appear only in second file.")
    print(unique_words2.difference(unique_words))
    print()

    print("Diplay words that appear in either first or second file, but not both.")
    print(unique_words.symmetric_difference(unique_words2))
    print()

# Calling the main function.
main()    