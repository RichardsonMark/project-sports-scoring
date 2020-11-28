class Team:
    def __init__(self, team_name, location, stadium_name, stadium_capacity, fixtures_played, fixtures_won, fixtures_drawn, fixtures_lost, points, id=None):
        self.team_name = team_name
        self.location = location
        self.stadium_name = stadium_name
        self.stadium_capacity = stadium_capacity
        self.fixtures_played = fixtures_played
        self.fixtures_won = fixtures_won
        self.fixtures_drawn = fixtures_drawn
        self.fixtures_lost = fixtures_lost
        self.points = points
        self.id = id