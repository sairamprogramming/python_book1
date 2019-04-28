# Word List File Reader.

def main():
    infile = open('word_list.txt', 'r') 

    word_count = 0
    longest_word = ''
    total_characters = 0

    for word in infile:
        word = word.rstrip('\n')
        word_count += 1
        if len(word) > len(longest_word):
            longest_word = word
        total_characters += len(word)
    
    infile.close()
    
    average_length_words = total_characters / word_count

    print("Number of words is file:", word_count)
    print("Longest word:", longest_word)
    print('Average word length:', format(average_length_words, '.2f'))

main()