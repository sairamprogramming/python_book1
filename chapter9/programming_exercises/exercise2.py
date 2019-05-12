# Implemented without using dictionries.

import random

def main():
    states, capitals = get_states_capitals('StatesCapitals.txt')

    total_questions = int(input("How many questions? "))
    correct_answers = 0

    for i in range(total_questions):
        q_number = random.randint(0, len(states))

        print('What is the capital of ' + states[q_number] +"?")
        answers = input("Ans: ")

        if answers.lower() == capitals[q_number].lower():
            correct_answers += 1
            print("You got the answer right!\n")
        else:
            print("You got the answer wrong!")
            print(capitals[q_number] + " is the capital of " + states[q_number] +'.\n')            

    print('\nThe total number of answers you got right is ' + str(correct_answers))            

def get_states_capitals(filename):
    infile = open(filename, 'r') 

    txt = []

    for line in infile:
        txt.append(line.strip())

    infile.close()
    
    capitals = []
    
    for index in range(0,len(txt),2):
        capitals.append(txt[index])

    states = []

    for index in range(1,len(txt),2):        
        states.append(txt[index])

    return states, capitals        

main()