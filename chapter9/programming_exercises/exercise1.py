# Program to define three respective dictionaries for jupiter's moons
# and print the key value pairs by getting key from the user.


def main():
    # In kilometers.
    moon_radius = {'io':1821.6,
                    'europa':1560.8,
                    'ganymede':2634.1,
                    'callisto':2410.3
                  }

    # In meter per second squared.
    moon_surface_gravity = {'io':1.796,
                            'europa':1.314,
                            'ganymede':1428,
                            'callisto':1.235
                            }                  

    # In days
    moon_orbital_periods = {'io':1.796,
                            'europa':3.551,
                            'ganymede':7.154,
                            'callisto':16.689}

    # Getting the key from the user.
    moon_name = input("Enter the name of jupiter's moon, you want information on: ")
    # To make the key value case - insensitive.
    moon_name = moon_name.lower()

    if moon_name in moon_radius:
        # The .captilize() method capitalizes a given string value.
        print(moon_name.capitalize(), "has a mean radius of", moon_radius[moon_name], "(in kilometers).")                                         
        print(moon_name.capitalize(), "has a surface gravity of", moon_surface_gravity[moon_name],
                "(in meters per second squared).")               
        print(moon_name.capitalize(), "has a orbital peroid of", moon_orbital_periods[moon_name], "(in days).")
    else:
        print("Given name is not jupiter's moon!")                        

# Calling the main function.
main()        