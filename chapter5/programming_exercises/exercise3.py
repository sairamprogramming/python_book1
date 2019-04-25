# How Much Insurance?

# Named constant is the minimum advised insurance purchase on the replacement cost.
INSURANCE_MINIMUM_PERCENTAGE = 0.80

# Defining the main function.
def main():
    home_cost = get_building_cost()
    insurance_on_home = minimum_insurance(home_cost)
    print('The minimum insurance on the home should be $', format(insurance_on_home, ',.2f'))

# Defining the get_building_cost function. 
# This function get the input from user. 
# This function also does input validation.
def get_building_cost():
    building_cost = float(input("Enter the replacement cost of the building: "))

    while building_cost < 0:
        print('Error!, replacement cost cannot be negative.')
        building_cost = float(input("Enter the replacement cost of the building: "))

    return building_cost

# Defining minimum_insurance function
# This fucntion calculates the minimum insurance amount
def minimum_insurance(replacement_cost):
    minimum_insurance_amount = replacement_cost * INSURANCE_MINIMUM_PERCENTAGE
    return minimum_insurance_amount

main()