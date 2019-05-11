# Expense Pie Chart

# Create a text file that contains your expenses for last month in the following categories:
#     Rent
#     Gas
#     Food
#     Clothing
#     Car payment
#     Misc
# Write a Python program that reads the data from the file and uses matplotlib to plot a pie
# chart showing how you spend your money.

import matplotlib.pyplot as plt

def main():
    # Getting values input from the user.
    rent = float(input('Enter rent: '))
    gas = float(input('Enter gas: '))
    food = float(input('Enter food: '))
    clothing = float(input('Enter clothing: '))
    car = float(input('Enter car payment: '))
    misc = float(input('Enter misc: '))

    prices = [rent, gas, food, clothing, car, misc]
    pie_labels = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc']
    
    # Creating the pie chart.
    plt.pie(prices, labels=pie_labels)

    # Pie chart title.
    plt.title("Expense Pie Chart")

    # Show the chart.
    plt.show()

# Calling the main function.
main()    