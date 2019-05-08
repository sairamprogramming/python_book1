dct1 = {'James':'Bond', 'a':2, 'b':3}
dct2 = {'a':1, 'b':2}

if 'James' in dct1:
    print("Value =",dct1['James'], ",This key is present in dct1.")
else:
    print('Key not found in dct1.')

if 'James' in dct2:
    print("Value =", dct2["James"], "This key is present in dct2.")
else:
    print('Key not found in dct2.')
