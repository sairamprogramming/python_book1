# Rainfall statistics.

# Program gets rainfall for 12 months in the year.
# Display the total rainfall for the year, average
# monthly rainfall, months with the highest and 
# lowest rainfall.

MONTHS_NUMBER = 12

def main():

    # Getting the rainfall for 12 months from the user.
    months_rainfall = [0] * MONTHS_NUMBER

    for index in range(MONTHS_NUMBER):
        months_rainfall[index] = float(input("Rainfall for month " + str(index + 1) + ": "))
    
    # Finding the total rainfall in the year.
    total_rainfall = 0.0

    for rainfall in months_rainfall:
        total_rainfall += rainfall
    
    # Finding the average monthly rainfall.
    average_rainfall = total_rainfall / MONTHS_NUMBER

    # Finding the minimum rainfall and the month.
    min_rainfall = months_rainfall[0]
    min_month = 1

    for index in range(len(months_rainfall)):
        if min_rainfall > months_rainfall[index]:
            min_rainfall = months_rainfall[index]
            min_month = index + 1

    # Finding the highest rainfall and the month.
    max_rainfall = months_rainfall[0]
    max_month = 1

    for index in range(len(months_rainfall)):
        if max_rainfall < months_rainfall[index]:
            max_rainfall = months_rainfall[index]
            max_month = index + 1

    # Display the output.
    print('Total Rainfall:', total_rainfall)
    print('Average monthly rainfall:', average_rainfall)
    print('Month with lowest rainfall:', min_month)
    print('Lowest Rainfall:', min_rainfall)
    print('Month with highest rainfall:', max_month)
    print("Highest Rainfall:", max_rainfall)

# Call the main function.
main()