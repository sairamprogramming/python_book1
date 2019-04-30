# Caesar Cipher.

# This part of the program creates a list of uppercase
# alphabets from the file alphabets.txt and stores it 
# in 'alpha_list' variable.
infile = open('alphabets.txt', 'r')

# This list holds the list of all alpahbets
# from a to z in uppercase.
alpha_list = []
alphabet = infile.readline()

while alphabet != '':
    alphabet = alphabet.rstrip('\n')
    alpha_list.append(alphabet)
    alphabet = infile.readline()

infile.close()

# Main program starts here.

def main():
    string_input = input('Enter the string to cipher: ')
    rotate_by = int(input('Shift amount: '))

    # Display the converted string.
    print(caesar_cipher(string_input, rotate_by))

# Function that implements the caesar cipher and
# returns the ciphered string.
def caesar_cipher(string, rotate):
    ciphered_string = ''

    for character in string:
        if character.isalpha():
            # Main part to convert string to ciphered string.
            index = alpha_list.index(character.upper())
            index = (index + rotate) % 26
            ciphered_string += alpha_list[index]
        else:
            ciphered_string += character

    return ciphered_string
        

# Calling the main function.
main()