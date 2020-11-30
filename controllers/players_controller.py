from flask import Blueprint, Flask, redirect, render_template, request

from models.player import Player
import repositories.player_repository as player_repository

players_blueprint = Blueprint("players", __name__)

# INDEX
@players_blueprint.route("/clubs/players")
def players():
    players = player_repository.select_all()
    return render_template("clubs/players/index.html", players=players)


# NEW
@players_blueprint.route("/clubs/players/new")
def new_player():
    return render_template("clubs/players/new.html")


# CREATE
@players_blueprint.route("/clubs/players", methods=["POST"])
def create_player():
    name = request.form["name"]
    player_info = request.form["player_info"]
    goals_scored = request.form["goals_scored"]
    new_player = Player(name, player_info, goals_scored)
    player_repository.save(new_player)
    return redirect("/clubs/players")


# EDIT
@players_blueprint.route("/clubs/players/<id>/edit")
def edit_player(id):
    player = player_repository.select(id)
    return render_template('clubs/players/edit.html', player=player)


# UPDATE
@players_blueprint.route("/clubs/players/<id>", methods=["POST"])
def update_player(id):
    name = request.form["name"]
    player_info = request.form["player_info"]
    goals_scored = request.form["goals_scored"]
    player = Player(name, player_info, goals_scored, id)
    player_repository.update(player)
    return redirect("/clubs/players")


# DELETE
@players_blueprint.route("/clubs/players/<id>/delete", methods=["POST"])
def delete_player(id):
    player_repository.delete(id)
    return redirect("/clubs/players")