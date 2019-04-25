# Automobile Costs

# Defining the main function.
def main():
    # Getting all the inputs from the user (with input validation)
    loan_payment_monthly = get_monthly_loan_payment()
    insurance_monthly = get_monthly_insurance()
    gas_cost_monthly = get_monthly_gas_cost()
    oil_cost_monthly = get_monthly_oil_cost()
    tires_cost_monthly = get_monthly_tires_cost()
    maintenance_cost_monthly = get_monthly_maintenance_cost()

    # Calcuating the total monthly cost
    total_monthly_cost = monthly_cost(loan_payment_monthly, insurance_monthly, gas_cost_monthly, oil_cost_monthly,
                                         tires_cost_monthly, maintenance_cost_monthly)
    
    # Calculating the annual cost by forecasting the total monthly cost.
    annual_cost_forecast = forecast_annual_cost(total_monthly_cost)

    # Displaying the output, monthly cost and annual cost.
    print('The total monthly cost is $', format(total_monthly_cost, ',.2f'))
    print("Annual cost forecast is $", format(annual_cost_forecast, ',.2f'))

# Function to caluclate the total monthly annual cost.
def monthly_cost(loan_payment, insurance, gas_cost, oil_cost, tire_cost, maintenance_cost):
    total_monthly_cost = loan_payment + insurance + gas_cost + oil_cost + tire_cost + maintenance_cost
    
    return total_monthly_cost

# Function calculates and returns the annual cost
def forecast_annual_cost(total_monthly_cost):
    annual_forecast = total_monthly_cost * 12

    return annual_forecast

# Function gets the monthly loan payment from the user.
def get_monthly_loan_payment():
    loan_payment = float(input("Enter the monthly loan payment: "))
    
    # Input validation.
    while loan_payment < 0:
        print("ERROR!, loan payment cannot be negative.")
        loan_payment = float(input("Enter the monthly loan payment: "))
    
    return loan_payment

# Function gets the monthly insurance from the user.
def get_monthly_insurance():
    insurance = float(input("Enter the monthly insurance: "))

    # Input validation.
    while insurance < 0:
        print("ERROR!, loan payment cannot be negative.")
        insurance = float(input("Enter the monthly insurance: "))
    
    return insurance

# Function gets the monthly gas cost from the user.
def get_monthly_gas_cost():
    gas_cost = float(input("Enter the monthly gas cost: "))  

    # Input validation.
    while gas_cost < 0:
        print("ERROR!, gas cost cannot be negative.")
        gas_cost = float(input("Enter the monthly gas cost: "))  
    
    return gas_cost

# Function gets the monthly oil cost from the user.
def get_monthly_oil_cost():
    oil_cost = float(input('Enter the monthly oil cost: '))

    # Input validation.
    while oil_cost < 0:
        print("ERROR!, gas cost cannot be negative.")
        oil_cost = float(input('Enter the monthly oil cost: '))
    
    return oil_cost

# Function gets the monthly tires cost from the user.
def get_monthly_tires_cost():
    tires_cost = float(input("Enter the monthly tires cost: "))

    # Input validation.
    while tires_cost < 0:
        print("ERROR!, oil cost cannot be negative.")
        tires_cost = float(input("Enter the monthly tires cost: "))
    
    return tires_cost

# Function gets the monthly maintenance cost from the user.
def get_monthly_maintenance_cost():
    maintenance_cost = float(input("Enter the monthly maintenance cost: "))

    # Input validation.
    while maintenance_cost < 0:
        print("ERROR!, oil cost cannot be negative.")
        maintenance_cost = float(input("Enter the monthly maintenance cost: "))
    
    return maintenance_cost
    
# Calling the main function.
main()