import unittest
from models.team import Team
from models.player import Player
from models.fixture import Fixture



class TestTeam(unittest.TestCase):
    def setUp(self):
        self.team1 = Team("Team 1", "Edinburgh, Scotland", "Murrayfield", 67000, 4, 0, 4, 0, 4)
        self.team2 = Team("Team 2", "Glasgow, Scotland", "Hampden", 52000, 4, 0, 4, 0, 4)
        self.fixture = Fixture(self.team1, self.team2)