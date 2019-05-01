# World Series Champions.

def main():
    infile = open('WorldSeriesWinners.txt', 'r')

    winners_list = []

    for line in infile:
        line = line.rstrip('\n')
        winners_list.append(line.lower())
    
    infile.close()

    # In this section we are getting the total list of teams in the series. (Assuming they won atleast one series).
    # Lazy method.
    teams_list = list(set(winners_list))
    # Sorting to get the order right evertime we run.
    teams_list.sort()

    # Printing teams in the series.
    print("Teams in series:")
    for team in teams_list:
        # .captilize() method captailize the words in the string.
        print(team.capitalize())
    print()

    # Getting the team to look up for, from the user.
    search_team = input("Enter the team you want to check: ")
    search_team = search_team.lower()

    # Counting the number of times the given team won the series.
    if search_team in teams_list:
        number_of_wins = 0

        for team in winners_list:
            if team == search_team:
                number_of_wins += 1
        
        print("The number of times", search_team, "won is", number_of_wins, '.')
    else:
        print("Given team is not in the series!")

# Calling the main function.
main()