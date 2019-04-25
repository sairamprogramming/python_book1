# Loan Payment Calcualtor.

def main():
    amount = get_amount()
    rate = get_rate()
    months = get_months()

    payment = payment_per_month(amount, rate, months) 

    print("The payment per month is $", format(payment, ',.2f'), sep = '')

def payment_per_month(amount, rate, months):
    return (rate * amount) / (1 - (1 + rate) ** -1)

def get_amount():
    amount = float(input("Enter the amount: "))

    while amount < 0:
        print("Error!, amount cannot be negative.")
        amount = float(input("Enter the amount: "))
    
    return amount

def get_rate():
    rate = float(input("Enter rate in percentage: "))

    while rate <= 0:
        print("ERROR!, rate cannot be negative or 0.")
        rate = float(input("Enter rate in percentage: "))
    
    # Convert to decimal.
    rate = rate / 100

    return rate

def get_months():
    months = int(input("Enter the number of months: "))

    while months < 0:
        print("ERROR!, months cannot be negative.")
        months = int(input("Enter the number of months: "))
    
    return months

main()
