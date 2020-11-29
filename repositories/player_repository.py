from db.run_sql import run_sql
from models.player import Player

def save(player):
    sql = "INSERT INTO players (name, player_info, goals_scored) VALUES (%s, %s, %s) RETURNING id"
    values = [player.name, player.player_info, player.goals_scored]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id


def select_all():
    players = []
    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for result in results:
        player = Player(result["name"], result["player_info"], result["goals_scored"], result["id"])
        players.append(player)
    return players


def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)
