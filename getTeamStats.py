def getTeamStats( teamname ):
    import csv
    with open('data/train/summary16_pt.csv') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            print ', '.join(row)

    return;


getTeamStats('Kansas')
