# Test Average and Grade.

# Defining the main funciton
def main():    
    # Getting scores input from the user.
    score1 = get_subject_score()
    score2 = get_subject_score()
    score3 = get_subject_score()
    score4 = get_subject_score()
    score5 = get_subject_score()

    # Determining the grade depending on the score
    grade1 = determine_grade(score1)
    grade2 = determine_grade(score2)
    grade3 = determine_grade(score3)
    grade4 = determine_grade(score4)
    grade5 = determine_grade(score5)

    # Calculating the average score of the five subjects.
    average = calc_average(score1, score2, score3, score4, score5)

    # Displaying the output.
    print("Grade in Subject 1:", grade1)
    print("Grade in Subject 2:", grade2)
    print("Grade in Subject 3:", grade3)
    print("Grade in Subject 4:", grade4)
    print("Grade in Subject 5:", grade5)

    print("The average is", format(average, '.2f'))

# This function gets the score input from the user.
def get_subject_score():
    score = float(input("Enter score: "))

    while score < 0  and score > 100:
        print("Invalid Inputs, try again")
        score = float(input("Enter score: "))
    
    return score

# This function determines the grade depending on the score and returns it.
def determine_grade(score):

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Calculates the average of 5 subjects and returns it.
def calc_average(score1, score2, score3, score4, score5):
    total = score1 + score2 + score3 + score4 + score5

    return total / 5

# Calling the main function.
main()