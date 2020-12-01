from db.run_sql import run_sql
from models.player import Player

def save(player):
    sql = "INSERT INTO players (name, player_info, goals_scored) VALUES (%s, %s, %s) RETURNING id"
    values = [player.name, player.player_info, player.goals_scored]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id
    return player


def select_all():
    players = []
    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for result in results:
        player = Player(result["name"], result["player_info"], result["goals_scored"], result["id"])
        players.append(player)
    return players


def select(id):
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    player = Player(result["name"], result["player_info"], result["goals_scored"], result["id"])
    return player


def update(player):
    sql = "UPDATE players SET (name, player_info, goals_scored) = (%s, %s, %s) WHERE id = %s"
    values = [player.name, player.player_info, player.goals_scored, player.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)