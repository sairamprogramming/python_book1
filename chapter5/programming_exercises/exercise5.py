# Property Tax.

# This constant represent, what percentage of acutal property tax is the assesment cost.
ACTUAL_ASSESMENT_PERCENTAGE = 0.60
# This constant is the property tax per 100$ 
PROPERTY_TAX_COSNTANT_DOLLAR = 0.72

# Defining the main function
def main():
    # Getting the actual property value form the user.
    actual_property_value = get_actual_property_value()

    # Calculating the assesment cost of the property
    property_assesment_cost = assesment_cost(actual_property_value)

    # Calculating the tax for the property.
    tax_on_property = property_tax(property_assesment_cost)

    # Display the output.
    print("The property tax is $", format(tax_on_property, ',.2f'), sep = '')

# This function gets actual property value form the user.
def get_actual_property_value():
    property_actual_value = float(input("Enter the actual value of the property: "))

    # Input Validation.
    while property_actual_value < 0:
        print("ERROR!, property catual value cannot be negative.")
        property_actual_value = float(input("Enter the actual value of the property: "))
    
    return property_actual_value

# This function calcualtes and returns the assesment cost.
def assesment_cost(property_actual_value):
    assesment = property_actual_value * ACTUAL_ASSESMENT_PERCENTAGE
    return assesment

# This function calculates and returns the property tax.
def property_tax(assesment_cost):
    tax = (assesment_cost * PROPERTY_TAX_COSNTANT_DOLLAR) / 100
    return tax

# Calling the main function.
main()
