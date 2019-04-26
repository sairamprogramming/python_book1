# Drawing pattern using nested loops.

for i in range(6):
    print('#', end = '')
    for i in range(i):
        print(' ', end = '')
    print('#')