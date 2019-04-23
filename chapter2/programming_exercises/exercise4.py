# Total purchase

SALES_PERCENT = 0.07

item1 = float(input("Enter the price of item: "))
item2 = float(input("Enter the price of item: "))
item3 = float(input("Enter the price of item: "))
item4 = float(input("Enter the price of item: "))
item5 = float(input("Enter the price of item: "))

sub_total = item1 + item2 + item3 + item4 + item5

total_payable_amount = sub_total * SALES_PERCENT

print("The total payable amount is", format(total_payable_amount, '.2f'))