from flask import Blueprint, Flask, redirect, render_template, request

from models.fixture import Fixture
import repositories.fixture_repository as fixture_repository
import repositories.player_repository as player_repository
import repositories.team_repository as team_repository

fixtures_blueprint = Blueprint("fixtures", __name__)

# INDEX
@fixtures_blueprint.route("/fixtures")
def fixtures():
    fixtures = fixture_repository.select_all()
    teams = team_repository.select_all()
    return render_template("fixtures/index.html", all_fixtures=fixtures, all_teams=teams)


# EDIT
@fixtures_blueprint.route("/fixtures/<id>/edit")
def edit_team(id):
    fixture = fixture_repository.select(id)
    teams = team_repository.select_all()
    return render_template('fixtures/edit.html', fixture=fixture, teams=teams)

# UPDATE
@fixtures_blueprint.route("/fixtures/<id>", methods=["POST"])
def update_team(id):
    team1 = request.form["team1"]
    team2 = request.form["team2"]
    
    fixture = Fixture(team1, team2, id)
    fixture_repository.update(fixture)
    return redirect("/fixtures")

# DELETE
@fixtures_blueprint.route("/fixtures/<id>/delete", methods=["POST"])
def delete_fixture(id):
    fixture_repository.delete(id)
    return redirect("/fixtures")

# SHOW
@fixtures_blueprint.route("/fixtures/<id>")
def show_fixture(id):
    fixture = fixture_repository.select(id)
    return render_template("fixtures/index.html", fixture=fixture)

# NEW
@fixtures_blueprint.route("/fixtures/new")
def new_fixture():
    return render_template("fixtures/new.html")    

# CREATE
@fixtures_blueprint.route("/fixtures", methods=["POST"])
def create_fixture():
    new_fixture = Fixture(team1 = request.form["team1"],
    team2 = request.form["team2"])
    fixture_repository.save(new_fixture)
    return redirect("/fixtures")
