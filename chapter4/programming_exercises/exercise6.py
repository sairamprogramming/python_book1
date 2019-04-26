# Miles to Kilmeters Table

# Miles to Kilometer converter constant
MILE_TO_KILOMETER_CONVERTER = 1.60934

# Heading of the table.
print("Miles\t\tKilometers")
print("-----\t\t----------")
# Loop to get the miles input required
for miles in range(10,81,10):
    # CAlculating kilometers
    kilometers = miles * MILE_TO_KILOMETER_CONVERTER
    # Displaying the output.
    print(miles, '\t\t', format(kilometers, '.2f'))