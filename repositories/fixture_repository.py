from db.run_sql import run_sql
from models.fixture import Fixture
from models.player import Player
import repositories.player_repository as player_repository
from models.team import Team
import repositories.team_repository as team_repository

def save(fixture):
    sql = "INSERT INTO fixtures (team1_id, team2_id) VALUES (%s, %s) RETURNING id"
    values = [fixture.team1.id, fixture.team2.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    fixture.id = id


def select_all():
    fixtures = []
    sql = "SELECT * FROM fixtures"
    results = run_sql(sql)
    for result in results:
        team1 = team_repository.select(result["team1_id"])
        team2 = team_repository.select(result["team2_id"])
        fixture = Fixture(team1, team2, result["id"])
        fixtures.append(fixture)
    return fixtures


def delete_all():
    sql = "DELETE FROM fixtures"
    run_sql(sql)