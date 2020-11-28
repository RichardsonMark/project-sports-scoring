import pdb

from models.fixture import Fixture
import repositories.fixture_repository as fixture_repository

from models.player import Player
import repositories.player_repository as player_repository

from models.team import Team
import repositories.team_repository as team_repository

fixture_repository.delete_all()
player_repository.delete_all()
team_repository.delete_all()

player_1 = Player("Maradona")
player_repository.save(human_1)

player_2 = Player("Pele")
player_repository.save(human_2)

player_3 = Player("Zidane")
player_repository.save(human_3)

player_4 = Player("Ronaldo (the Brazilian one!)")
player_repository.save(human_4)

team_1 = Team("Melchester Rovers")
zombie_repository.save(zombie_1)

team_2 = Team("The Hurricanes")
team_repository.save(zombie_2)

team_3 = Team("Team Shaolin")
zombie_repository.save(zombie_3)

team_4 = Team("Harchester United")
team_repository.save(zombie_4)

fixture_1 = Biting(team_1, team_2)
fixture_repository.save(fixture_1)

fixture_2 = Biting(team_3, team_4)
fixture_repository.save(fixture_2)

fixture_3 = Biting(team_1, team_3)
fixture_repository.save(fixture_3)

fixture_4 = Biting(team_2, team_4)
fixture_repository.save(fixture_4)

pdb.set_trace()
