class Fixture:
    def __init__(self, team1, team2, id=None):
        self.team1 = team1
        self.team2 = team2
        self.id = id

# function to set up a fixture
    def setup_fixture(self, team1, team2):
        return "{team1.team_name}" + "v" + "{team2.team_name}"

 
# this function determines the winner of the fixture
    def determine_winner(self, team1, team2):
        if self.team1.score == self.team2.score:
            return "Draw"
        elif self.team1.score > self.team2.score:
            return "Team 1"
        elif self.team1.score < self.team2.score:
            return "Team 2"


#this function adds the points won to the team total
#    def add_points(self):