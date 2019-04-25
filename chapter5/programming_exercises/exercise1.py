# Kilometer Converter

# Named constant has to be multiplied with kilometer to get miles.
MILE_KILOMETER_CONVERTER = 0.6214

# Defining the main function.
def main():
    # Getting kilometers from the user.
    kilometer_input = float(input("Enter the distance( in kilometers): "))
    
    # Calling convert_km_to_miles funtion and printing the output.
    miles = convert_km_to_miles(kilometer_input)
    print(kilometer_input, " km converted to miles is", format(miles, '.4f'), 'miles')

# Defining convert_km_to_miles function.
def convert_km_to_miles(kilometers):
    miles = kilometers *  MILE_KILOMETER_CONVERTER
    return miles

# Calling the main function.
main()