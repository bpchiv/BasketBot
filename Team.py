class Team:
    TeamName='Placeholder'
    Tempo=0
    RankTempo=0
    AdjTempo=0
    RankAdjTempo=0
    OE=0
    RankOE=0
    AdjOE=0
    RankAdjOE=0
    DE=0
    RankDE=0
    AdjDE=0
    RankAdjDE=0
    EM=0
    RankEM=0

    def __init__(self, data):
        ##Initializes class with data being a row of data, in the order above
        self.TeamName= data[0]
        self.Tempo=data[1]
        self.RankTempo=data[2]
        self.AdjTempo=data[3]
        self.RankAdjTempo=data[4]
        self.OE=data[5]
        self.RankOE=data[6]
        self.AdjOE=data[7]
        self.RankAdjOE=data[8]
        self.DE=data[9]
        self.RankDE=data[10]
        self.AdjDE=data[11]
        self.RankAdjDE=data[12]
        self.EM=data[13]
        self.RankEM=data[14]
