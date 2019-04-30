# Average number of words.

# This program reads a file and finds the average number of words in a sentence.

def main():
    # Open the file in read mode.
    infile = open('text.txt', 'r')

    # Initalizing the starting conditions.
    line = infile.readline()
    line_count = 0
    total_words = 0

    # Count total lines and total number of words in the file.
    while line != '':
        line = line.split()
        total_words += len(line)
        line_count +=1   

        line = infile.readline()
    
    # Close the file.
    infile.close()

    # Calcuate and display the average number of words in a sentence.
    average_words = total_words / line_count
    print('Average number of words per sentence is',
            format(average_words, '.2f'))

# Call the main function.
main() 