# Morse Code Converter.

# This part of the program creates a list mapping
# characters to it's respective morse code.
# From the file 'morse_code.txt'.
morse_code = []

infile = open('morse_code.txt', 'r')

for line in infile:
    line = line.rstrip('\n')
    line = line.split()
    morse_code.append(line)

morse_code.append([" ", " "])

infile.close()

# This is the main part of the program that converts string to morse code.
def main():
    # Get string input from the user.
    string_input = input("Enter string: ")

    # Initalize variable that will hold the morse code.
    morse_string = ''

    # Coverting given string to morse code.
    for charcter in string_input:
        for index in range(len(morse_code)):
            if morse_code[index][0] == charcter.upper():
                morse_string += morse_code[index][1]
                break
    
    # Displaying the output.
    print(morse_string)

# Calling the main function.
main()