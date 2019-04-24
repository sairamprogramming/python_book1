# Time Converter.

# Named constant, that are converter day, hour, minute in seconds
MINUTES_IN_SECONDS = 60
HOUR_IN_SECONDS = 3600
DAY_IN_SECONDS = 86400

# Getting the number of seconds from the user.
seconds_input = int(input('Enter the number of seconds: '))

# Calculating minutes and seconds form given input. (only is sec >= 60 and sec <= 3600)
# Ending condition is so that we do not do the similar calculations multiple times. 
if seconds_input >= MINUTES_IN_SECONDS and seconds_input < HOUR_IN_SECONDS:
    minutes = seconds_input // MINUTES_IN_SECONDS
    seconds_left = seconds_input % MINUTES_IN_SECONDS
    
    # Displaying the output. (minutes and seconds)
    print(seconds_input, "converted to minutes is", minutes, "minutes and", seconds_left, "seconds")

# Calculating hours, minutes and seconds form given input. (only is sec >= 3600 and sec <= 86400)
if seconds_input >= HOUR_IN_SECONDS and seconds_input < DAY_IN_SECONDS:
    hours = seconds_input // HOUR_IN_SECONDS
    seconds_left = seconds_input % HOUR_IN_SECONDS
    minutes = seconds_left // MINUTES_IN_SECONDS
    seconds_left = seconds_left % MINUTES_IN_SECONDS

    # Displaying the output. (hours, minutes and seconds)
    print(seconds_input, "converted to hours:")
    print(hours, "hours", minutes, "minutes and", seconds_left, "seconds")

# Calculating days, hours, minutes and seconds form given input. (only if sec >= 86400)
if seconds_input >= DAY_IN_SECONDS:
    days = seconds_input // DAY_IN_SECONDS
    seconds_left = seconds_input % DAY_IN_SECONDS
    hours = seconds_left // HOUR_IN_SECONDS
    seconds_left = seconds_left % HOUR_IN_SECONDS
    minutes = seconds_left // MINUTES_IN_SECONDS
    seconds_left = seconds_left % MINUTES_IN_SECONDS

    # Display the output. (days, hours, minutes and seconds)
    print(seconds_input, "converted to days")
    print(days, "days,", hours, "hours,", minutes, "minutes and", seconds_left, "seconds")