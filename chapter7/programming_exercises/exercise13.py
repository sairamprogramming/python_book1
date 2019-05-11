# Magic 8 ball.

# Write a program that simulates a Magic 8 Ball, which is a fortune-telling toy that displays a
# random response to a yes or no question. In the student sample programs for this book, you
# will find a text file named 8_ball_responses.txt . The file contains 12 responses, such
# as “I don’t think so”, “Yes, of course!”, “I’m not sure”, and so forth. The program should
# read the responses from the file into a list. It should prompt the user to ask a question, then
# display one of the responses, randomly selected from the list. The program should repeat
# until the user is ready to quit.

import random

def main():
    # Getting the list of choices from the file and 
    # making a list.
    infile = open('8_ball_responses.txt', 'r')

    lst = []

    for line in infile:
        lst.append(line.strip())   

    infile.close()

    # Getting the question and giving back the random
    # answer.
    input("Enter a question: ")

    choice = random.randint(0, len(lst) - 1)

    print(lst[choice])    

main()    