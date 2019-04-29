# Program to convert numeric date to string format.
# example 03/12/2018 --> March 12, 2018

# Creathing months tuple to access month names form the date.
months = [0,]

infile = open('months.txt', 'r')

for line in infile:
    line = line.strip()
    months.append(line)

infile.close()

MONTHS = tuple(months)

def main():
    try:
        date = input('Enter date(mm/dd/yy): ')

        month,day,year = date.split('/')

        print(MONTHS[int(month)], day + ',', year)
    except:
        print('Invalid Input')

main()