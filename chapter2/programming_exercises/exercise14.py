# Compound interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate: "))
number_per_year = int(input("Number of times the interest is compounded: "))
time = int(input("Enter the number of years: "))

amount = principal*((1 + rate / number_per_year) ** (number_per_year * time))

print("The amount compounded is", format(amount, ',.2f'))