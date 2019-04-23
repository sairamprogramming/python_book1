# Payment Instalments

INTEREST = 0.05

total_amount = float(input('Enter the total payble amount: '))
number_of_installments = int(input('Enter the number of installments: '))

total_interest = total_amount * INTEREST
total_amount = total_amount + total_interest

installment_amount = total_amount / number_of_installments

print("The total cost is", format(total_amount, ',.2f'),
        ". Each installment is", format(installment_amount, ',.2f'))