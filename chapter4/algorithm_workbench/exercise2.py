keep_going = 'y'

while keep_going == 'y':
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    print("The sum of two numbers is", num1 + num2)

    keep_going = input('Do you want to continue(y for yes)? ')
