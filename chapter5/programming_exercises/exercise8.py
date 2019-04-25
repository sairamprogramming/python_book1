# Paint job estimator.

# Defining the main function.
def main():
    # Getting input from the user, wall space and paint price.
    wall_space = get_wall_space()       # in square feet
    paint_price = get_paint_price()     # per gallon

    # Calculating all required.
    gallons_required = gallons(wall_space)
    labour_hours = hours_of_labour(wall_space)
    paint_cost = paint(gallons_required, paint_price)
    labour_charges = labour_price(labour_hours)
    total_cost = total_price(paint_cost, labour_charges)

    print("Number of gallons:", gallons_required)
    print("Hours of labour required:", labour_hours)
    print("Cost of paint: $", format(paint_cost, ',.2f'), sep = '')
    print("Labour Charges: $", format(labour_charges, ',.2f'), sep = '')
    print("The total cost of the pain job is $ ", format(total_cost, ',.2f'), sep = '')

def total_price(paint_cost, labour_charges):
    return paint_cost + labour_charges

def labour_price(labour_hours):
    return 35 * labour_hours

def paint(gallons_required, paint_price):
    return gallons_required * paint_price

def hours_of_labour(wall_space):
    return (wall_space * 8) / 112

def get_wall_space():
    wall_space = float(input("Enter wall space(in square feet): "))

    while wall_space < 0:
        print("ERROR!, wall space cannot be negative or 0.")
        wall_space = float(input("Enter wall space(in square feet): "))
    
    return wall_space

def get_paint_price():
    paint_price = float(input("Enter pain price(per gallon): "))

    while paint_price < 0:
        print("ERROR!, paint price cannot be negative.")
        paint_price = float(input("Enter pain price(per gallon): "))
    
    return paint_price

def gallons(wall_space):
    return wall_space / 112

main()