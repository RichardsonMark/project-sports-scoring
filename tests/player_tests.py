import unittest
from app.models.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.rps_player = Player("Diego Maradona", "Squad No: 10 - Flawed genius, one of the all time greats", 550)


    @unittest.skip("Delete this line to run the test")
    def test_player_has_name(self):
        self.assertEqual("Diego Maradona", self.player.name)

    @unittest.skip("Delete this line to run the test")
    def test_player_has_inf(self):
        self.assertEqual("Squad No: 10 - Flawed genius, one of the all time greats", self.player.player_info)

    @unittest.skip("Delete this line to run the test")
    def test_player_has_games_played(self):
        self.assertEqual("600", self.player.games_played)