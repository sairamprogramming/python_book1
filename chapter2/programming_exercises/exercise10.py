# Ingredient Adjuster

sugar_each_cookie = 1.5 / 48.0
butter_each_cookie = 1.0 / 48.0
flour_each_cookie = 2.75 / 48.0

number_of_cookies = float(input("Enter number of cookies: "))

total_sugar = number_of_cookies * sugar_each_cookie
total_butter = number_of_cookies * butter_each_cookie
total_flour = number_of_cookies * flour_each_cookie

print("The ingredients for " + format(number_of_cookies, '.0f') + ":")
print(format(total_sugar, '.2f'), "cups of sugar.")
print(format(total_butter, '.2f'), "cup of butter.")
print(format(total_flour, '.2f'), "cups of flour.")