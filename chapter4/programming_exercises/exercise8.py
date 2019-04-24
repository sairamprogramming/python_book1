# Average Word Length

# Assigned an initial value (garbage value), will be over written in while loop.
word = "intial temporary holder."

# Initalizing Accumulators
total_words = 0
total_length = 0

# Getting input of words from the user.
while word != '':
    word = input("Enter a word('' to exit): ")

    # This is necessary as we do not want total_words to accumulate when exit conditon is input
    # This also gives us the correct word average.
    if word == '':
        continue

    total_words += 1
    total_length += len(word)
    print(total_length, total_words)

# Calculating the average word length from the given words.
average_length = total_length // total_words

# Displaying the output.
print("Average word length is", average_length)