# Software Sales.

# Named constant holds the retail price of each unit.
RETAIL_PRICE = 99.0

# Getting input from the user on the number of units purchsed.
units_purchased = int(input('Number of units purchased: '))

# Initalzing discount variable, this holds the discount percentage
discount = 0.0

# Assigning the discount percentage based on number of unit purchased.
if units_purchased >= 10 and units_purchased <= 19:
    discount = 0.1  # 10%
elif units_purchased >= 20 and units_purchased <= 49:
    discount = 0.2  # 20 %
elif units_purchased >= 50 and units_purchased <= 99:
    discount = 0.3  # 30%
elif units_purchased >= 100:
    discount = 0.4  # 40%

# Calculating the amount discounted and the amount to pay after discount.
total_price = units_purchased * RETAIL_PRICE
discount_amount =  total_price * discount
pay_after_discount = total_price - discount_amount

# Display the discount and payable amount after discount.
print("The discount given is $", format(discount_amount, ',.2f'), sep='')
print("The total payable amount is $", format(pay_after_discount, ',.2f'), sep='')