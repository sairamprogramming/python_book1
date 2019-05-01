# Driver's Licence Exam.

# List holds the correct answers
CORRECT_ANSWERS = ['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']

def main():
    # Open file in read mode
    infile = open('student_answers.txt', 'r')

    answers = []

    # Bulid list of all students solutions from the file.
    for item in infile:
        item = item.rstrip('\n')
        answers.append(item)
    
    # Close the file.
    infile.close()

    # Accumulator to count the number of correct answers.
    number_correct_answers = 0
    
    # Getting the total number of correct answers.
    try:
        for index in range(len(CORRECT_ANSWERS)):
            if answers[index] == CORRECT_ANSWERS[index]:
                number_correct_answers += 1
    except IndexError:
        print('The file you have entered does not have the correct number of answers.')
        return
        
    # Displaying the appropriate choice.
    if number_correct_answers >= 15:
        print("You have passed the test.")
    else:
        print("You have not passed the test.")

import random

# This function creates a random students solution file.
# Good chance will never pass the test in main()
def create_student_solutions():
    answer_choice = ['A', 'B', 'C', 'D']

    solutions = []

    for i in range(len(CORRECT_ANSWERS)):
        solutions.append(answer_choice[random.randint(0, 3)])

    outfile = open('student_answers.txt', 'w')

    for item in solutions:
        outfile.write(item + '\n')

    outfile.close()
    print("student_answers.txt file is created.")

# Will most probably pass the test with this solution.
create_student_solutions()
# Calling the main function.
main()    