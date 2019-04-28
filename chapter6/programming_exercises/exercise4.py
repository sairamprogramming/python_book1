# High Score.
def main():
    infile = open('scores.txt', 'r')

    highest_score = 0
    highest_score_name = ''
    count_records = 0

    name = infile.readline()

    while name != '':
        score = float(infile.readline())

        if highest_score < score:
            highest_score_name = name.rstrip('\n')
            highest_score = score
        
        count_records += 1
        name = infile.readline()
    
    print('The highest score in file is:')
    print(highest_score_name)
    print(highest_score)

    print()

    print('The total records is', count_records)

main()