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


def compareTeams( team1, team2):
    val=0
    val=val+(team1.RankTempo - team2.RankTempo)
    val=val+(team1.RankAdjTempo - team2.RankAdjTempo)
    val=val+(team1.RankOE - team2.RankDE)
    val=val+(team1.RankAdjOE - team2.RankAdjDE)

    if(abs(val) < 200):
        if(team1.RankEM > team2.RankEM):
            return team1.TeamName
        else:
            return team2.TeamName
    return val;

Cal = getTeamStats('Syracuse')
Hawaii = getTeamStats('North Carolina')

print(Cal.TeamName)
print(Hawaii.TeamName)

print(compareTeams( Cal, Hawaii))
