import unittest
from app.models.team import Team
from app.models.player import Player


class TestTeam(unittest.TestCase):
    def setUp(self):
        self.team1 = Team("Team 1", 2)
        self.team2 = Team("Team 2", 1)
        self.fixture = Fixture(self.team1, self.team2)