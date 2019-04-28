infile = open('steps.txt', 'r')

count = 0

steps = infile.readline()

while steps != '':
    steps = infile.readline()
    count += 1

print(count)
