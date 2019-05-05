# This program displays the gross pay. (Input validation requirements demonstration).
 
# Get the number of hours worked.
hours = int(input('Enter the hours worked this week: '))

# get the hourly pay rate.
pay_rate = float(input('Enter the hourly pay rate: '))

# Calculate the gross pay.
gross_pay = hours * pay_rate

# Display the gross pay.
print('Gross pay: $', format(gross_pay, ',.2f'), sep ='')