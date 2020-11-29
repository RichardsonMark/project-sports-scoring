from flask import Blueprint, Flask, redirect, render_template, request

from models.team import Team
import repositories.team_repository as team_repository

teams_blueprint = Blueprint("teams", __name__)

# INDEX
@teams_blueprint.route("/clubs")
def teams():
    teams = team_repository.select_all()
    return render_template("clubs/index.html", teams=teams)