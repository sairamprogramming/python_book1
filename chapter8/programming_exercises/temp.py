import os

def main():
    infile = open('months.txt', 'r')

    temp_file = open('temp.txt', 'w')

    for line in infile:
        line = line.strip()
        line = line.split()
        temp_file.write(line[0] + '\n')
    
    infile.close()
    temp_file.close()

    os.remove('months.txt')
    os.rename('temp.txt', 'months.txt')

main()