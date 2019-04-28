# Average Steps Taken
# Program to find the average steps taken per month.

def main():
    # Opening the step file.
    infile = open('steps.txt', 'r')

    # Initalizing the month variable
    month = 0

    # Getting the average number of steps for each month.
    while month < 12:
        month += 1
        print('month :', end='')
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            average_month_steps = get_average(infile, 31)
            print(month, format(average_month_steps, '.2f'))
        elif month == 2:
            average_month_steps = get_average(infile, 28)
            print(month, format(average_month_steps, '.2f'))
        else:
            average_month_steps = get_average(infile, 30)
            print(month, format(average_month_steps, '.2f'))
        
    # Closing the file.    
    infile.close()
    print('Output has been displayed.')
        

# Function to get the average number of steps of each month.

# Takes 2 arguments, 1st file object to read inputs from the file
# 2nd the number od days in the particular month.
def get_average(file_object, days):
    count = 0
    total = 0.0
    
    # Getting the total number of steps in the month.
    while count < days:
        steps = file_object.readline()
        count += 1
        steps = int(steps)
        total += steps
        
        
    # Calculating the average
    average = total / days
    
    # Returning the average.
    return average

# Calling the main function.
main()
            