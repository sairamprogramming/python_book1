# Dice Rolling Function.

# Program simulates dice throw.
import random

def main():
    # Getting a positive integer(number of throws) from the user.
    # Exception handiling
    incorrect_input = True

    while incorrect_input:
        try:
            number_of_throws = int(input('Enter number of throws: '))

            while number_of_throws < 0:
                print('Enter a positive integer!')
                number_of_throws = int(input('Enter number of throws: '))
            
            incorrect_input = False
        except Exception as err:
            print(err)
            print('Enter number of throws again!')
    

    # Getting the number of dice rolls for the number of throws.
    dice_rolls = roll(number_of_throws)

    # Displaying the output.
    print('The dice rolls are:')
    print(dice_rolls)

# Function gets the dice rolls list and returns it.
def roll(number_of_throws):
    dice_rolls = []

    index = 0
    while index < number_of_throws:
        dice_rolls.append(random.randint(1, 6))
        index += 1
    
    return dice_rolls

# Call the main function.
main()