# Average Rainfall

# Get the number of years from the user.
number_of_years = int(input("Enter the number of years data is collected: "))

# Initalizing total rainfall accumulator and variable 'month' to find the number of months the data is collected.
total_rainfall = 0.0
month_accumulator = 0

# Getting input on the rainfall for each month and calculating total_rainfall.
for year in range(1,number_of_years+1):
    for month in range(1,13):
        month_rainfall = float(input("Inches of rainfall for year " +  str(year) + " and month " + str(month) + ": "))
        total_rainfall += month_rainfall
        month_accumulator += 1

# Calculating average rainfall per month.
average_rainfall = total_rainfall / month_accumulator

# Displaying the output.
print("Output:")
print("\tTotal Rainfall:", total_rainfall)
print("\tAverage Rainfall:", format(average_rainfall, '.2f'))
print("\tTotal months:", month_accumulator)