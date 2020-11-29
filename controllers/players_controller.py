from flask import Blueprint, Flask, redirect, render_template, request

from models.player import Player
import repositories.player_repository as player_repository

players_blueprint = Blueprint("players", __name__)

# INDEX
@players_blueprint.route("/clubs/players")
def players():
    players = player_repository.select_all()
    return render_template("clubs/players/index.html", players=players)

