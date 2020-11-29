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
    return render_template("fixtures/index.html", fixtures=fixtures)