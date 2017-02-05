from Team import Team

##Gets team stats from CSV file
## YEAR IS HARD CODED
def getTeamStats( teamname ):
    import csv
    ##YEAR/FILE is hard coded below
    with open('data/train/summary16_pt.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            if( row[0] == teamname ):
                return Team(row)

    return;


Kansas = getTeamStats('Kansas')
print(Kansas.Tempo)
