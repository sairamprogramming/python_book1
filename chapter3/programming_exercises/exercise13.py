# Shipping Charges.

# Getting package weight from the user.
package_weight = float(input("Enter the weight of package(pounds): "))

# Assiging rate per pound depending on the package weight.
if package_weight > 0 and package_weight <= 2:
    rate = 1.5
elif package_weight > 2 and package_weight <= 6:
    rate = 3.0
elif package_weight > 6 and package_weight <= 10:
    rate = 4.0
elif package_weight > 10:
    rate = 4.75

# Calculating the shipping charges.
shipping_price = package_weight * rate

# Displaying the shipping charges.
print('Shipping Charges: $', format(shipping_price, ',.2f'), sep='')