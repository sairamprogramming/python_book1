# Pound to Kilogram conversion

POUND_KILO_CONVERSION_MULTIPLE = 0.454

pounds = float(input("Enter the amount of pounds to convert: "))

kilograms = pounds *  POUND_KILO_CONVERSION_MULTIPLE

print(format(pounds, '.2f'), "converted to kilograms is", format(kilograms, '.2f'))
