# Oceans Level

# This Constant holds the increase ocean level yearly.
INCREASE_PER_YEAR = 1.6     # in millimeters

# Initializing the ocean level increase yearly accumulator.
ocean_level_increase = 0

# We need to find the ocean level increase for 25 years
for year in range(1, 26):
    # Calculating the yearly ocean level increase.
    ocean_level_increase += INCREASE_PER_YEAR

    # Display the output
    print('Year', year, 'Ocean Level Increase:', format(ocean_level_increase, '.2f'), 'millimeters.')