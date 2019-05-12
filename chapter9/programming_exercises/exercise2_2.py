# Implemented using dictionries.

import random

def main():
    # Getting the dictionary of captial: state form.    
    capitals = get_states_capitals('StatesCapitals.txt')

    # Getting the total number of questions in the quiz.
    total_questions = int(input("How many questions? "))
    correct_answers = 0

    # Main body of the program which formuates questions,
    # ask the user of the answer and checks if the given
    # answer is correct.
    for unused_variable in range(total_questions):
        q_number = random.randint(0, len(capitals))
        capital = list(capitals.keys())[q_number]
        state = capitals[capital]

        print('What is the capital of ' + state +"?")
        answers = input("Ans: ")

        if answers.lower() == capital.lower():
            correct_answers += 1
            print("You got the answer right!\n")
        else:
            print("You got the answer wrong!")
            print(capital + " is the capital of " + state +'.\n')            

    print('\nThe total number of answers you got right is ' + str(correct_answers))            

# This function returns a dictonary of capitals:states
# to the calling function.
def get_states_capitals(filename):
    infile = open(filename, 'r') 

    capitals_dict = {}

    line = infile.readline()
    
    while line != '':
        capitals_dict[line.strip()] = infile.readline().strip()
        line = infile.readline()

    infile.close()
    
    return capitals_dict

# Calling the main function
main()