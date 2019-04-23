# Tip, Tax and Total

TIP_PERCENT = 0.18
SALES_TAX = 0.07

meal_price = float(input("Enter the meal price: "))

total_sales_tax = meal_price * SALES_TAX
total_tip = meal_price * TIP_PERCENT

total_payable_amount = meal_price + total_sales_tax + total_tip

print("The total sales tax is", format(total_sales_tax, '.2f'))
print("The total tip is", format(total_tip, '.2f'))
print("The total amount to pay is", format(total_payable_amount, '.2f'))