# Grade calculator

# Getting input from the user
test1 = int(input("Enter the marks obtained in test 1: "))
test2 = int(input("Enter the marks obtained in test 2: "))
main_exam = int(input('Enter the marks obtained in the main exam: '))

total_marks = test1 + test2 + main_exam

# Checking if input are within expected range of each variable.
if (test1 < 0 or test1 > 25) or (test2 < 0 or test2 > 25) or (main_exam < 0 or main_exam >  50):
    print("You have entered invalid inputs.")
else:
    # Printing the grade for the corresponding marks.
    if total_marks < 50 or main_exam < 25:
        print("Total Points:",total_marks,"and Grade: Fail")
    elif total_marks > 80:
        print("Total Points:",total_marks,"and Grade: Distinction")
    elif total_marks > 60:
        print("Total Points:",total_marks,"and Grade: Credit")
    else:
        print("Total Points:",total_marks,"and Grade: Pass")