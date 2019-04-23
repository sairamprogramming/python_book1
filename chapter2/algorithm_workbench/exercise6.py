# Simple assignment and math operation.

down_payment = float(input('Enter the down payment: '))

total = float(input('Enter the total payable amount: '))

due = total - down_payment

print("The due remaining is $", format(due, '.2f'))
