import pdb

from models.fixture import Fixture
import repositories.fixture_repository as fixture_repository

from models.player import Player
import repositories.player_repository as player_repository

from models.team import Team
import repositories.team_repository as team_repository

# fixture_repository.delete_all()
# player_repository.delete_all()
team_repository.delete_all()

# player_1 = Player("Maradona")
# player_repository.save(player_1)

# player_2 = Player("Pele")
# player_repository.save(player_2)

# player_3 = Player("Zidane")
# player_repository.save(player_3)

# player_4 = Player("Ronaldo (the Brazilian one!)")
# player_repository.save(player_4)

# player_5 = Player("Ibrahimovic")
# player_repository.save(player_5)

team_1 = Team("Napoli", "Naples, Italy", "Stadio San Paolo", 60000, 4, 0, 4, 0, 4, 0)
team_repository.save(team_1)

team_2 = Team("Santos", "Sao Paulo, Brazil", "Estádio Urbano Caldeira (Vila Belmiro)", 16000, 4, 0, 4, 0, 4, 0)
team_repository.save(team_2)

team_3 = Team("Juventus", "Turin, Italy", "Juventus Stadium", 41000, 4, 0, 4, 0, 4, 0)
team_repository.save(team_3)

team_4 = Team("Barcelona", "Barcelona, Catalonia, Spain", "Camp Nou", 99000, 4, 0, 4, 0, 4, 0)
team_repository.save(team_4)

team_5 = Team("AC Milan", "Milan, Italy", "Stadio Giuseppe Meazza (San Siro)", 80000, 4, 0, 4, 0, 4, 0)
team_repository.save(team_5)

# fixture_1 = Fixture(team_1, team_2)
# fixture_repository.save(fixture_1)

# fixture_2 = Fixture(team_3, team_4)
# fixture_repository.save(fixture_2)

# fixture_3 = Fixture(team_1, team_3)
# fixture_repository.save(fixture_3)

# fixture_4 = Fixture(team_2, team_4)
# fixture_repository.save(fixture_4)

pdb.set_trace()
