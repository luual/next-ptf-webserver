"""
Define the blueprint for the team routes
"""

from flask import Blueprint
from flask_restful import Api

from src.services.teams.resources import TeamsResource, TeamResource

TEAMS_BLUEPRINT = Blueprint("teams", __name__)
Api(TEAMS_BLUEPRINT).add_resource(TeamsResource, "/teams")

TEAM_BLUEPRINT = Blueprint('team', __name__)
Api(TEAM_BLUEPRINT).add_resource(TeamResource, "/teams/<int:team_id>")