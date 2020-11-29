from flask import Blueprint, Flask, redirect, render_template, request

from models.team import Team
import repositories.team_repository as team_repository

teams_blueprint = Blueprint("teams", __name__)

# INDEX
@teams_blueprint.route("/clubs")
def teams():
    teams = team_repository.select_all()
    return render_template("clubs/index.html", teams=teams)


# EDIT
@teams_blueprint.route("/clubs/<id>/edit")
def edit_team(id):
    team = team_repository.select(id)
    return render_template('clubs/edit.html', team=team)

# UPDATE
@teams_blueprint.route("/clubs/<id>", methods=["POST"])
def update_team(id):
    team_name = request.form["team_name"]
    location = request.form["location"]
    stadium_name = request.form["stadium_name"]
    stadium_capacity = request.form["stadium_capacity"]
    fixtures_played = request.form["fixtures_played"]
    fixtures_won = request.form["fixtures_won"]
    fixtures_drawn = request.form["fixtures_drawn"]
    fixtures_lost = request.form["fixtures_lost"]
    points = request.form["points"]
    score = request.form["score"]
    
    team = Team(team_name, location, stadium_name, stadium_capacity, fixtures_played, fixtures_won, fixtures_drawn, fixtures_lost, points, score, id)
    team_repository.update(team)
    return redirect("/clubs")


# DELETE
@teams_blueprint.route("/clubs/<id>/delete", methods=["POST"])
def delete_team(id):
    team_repository.delete(id)
    return redirect("/clubs")


# SHOW
@teams_blueprint.route("/clubs/<id>")
def show_team(id):
    team = team_repository.select(id)
    return render_template("clubs/players/index.html", team=team)