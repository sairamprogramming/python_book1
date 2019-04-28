# Program displays the all the entries in golf.txt

def main():
    # Opening the file in read mode.
    infile = open('golf.txt', 'r')

    # Getting the intial name.
    name = infile.readline()

    # Getting name and score and printing to output.
    while name != '':
        name = name.rstrip('\n')
        score = infile.readline().rstrip('\n')
        
        print(name)
        print(score)
        print()

        name = infile.readline()

    # Closing the file.
    infile.close()    
    print('Displayed all items in file golf.txt')

# Calling the main funciton.
main()
