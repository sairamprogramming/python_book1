# See what the code prints

try:
    x = float('123abc')
    print(x)
except ValueError:
    print('This code caused a ValueError.')
except TypeError:
    print('This code caused a TypeError.')
except NameError:
    print('This code caused a NameError.')
print('The end.')