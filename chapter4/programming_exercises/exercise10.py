# Tution Increase.

# Constants hold, the starting tution amount, the percentage by which tution increases yearly
#  and the number of years that we need to find the tution amount.
CURRENT_TUTION = 8000
INCREASE_RATE = .03
NUMBER_OF_YEARS = 5

# Initalizing the 'tution_amount variable. Printing the starting tution amount.'
tution_amount = CURRENT_TUTION
print('Tution amount at the start is $', format(tution_amount, ',.2f'), sep = '')

# Calculating and printing the tution amount increase for all the years.
for year in range(1, NUMBER_OF_YEARS + 1):
    tution_amount += tution_amount + INCREASE_RATE

    print('Tution amount for after ', year, ' is $', format(tution_amount, ',.2f'), sep = '')

