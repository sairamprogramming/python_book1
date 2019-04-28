# Program to write record(name and score) to golf.txt

def main():
    # Opening the file in append mode.
    outfile = open('golf.txt', 'a')

    # Getting the player name and score from the user.
    player_name = input('Enter the players name: ')
    score = get_score()

    # Writing values to the file.
    outfile.write(player_name + '\n')
    outfile.write(str(score) + '\n')
    
    # Closing the file.
    outfile.close()
    print('The file has been updated.')

# A good way to handle exceptions during input of values and getting the correct input.
def get_score():
    good_input = True

    while good_input:
        try:
            score_input = float(input('Enter the players socre: '))
            good_input = False
        except:
            print("Enter Valid Input.")
    
    return score_input

# Call the main function.
main()