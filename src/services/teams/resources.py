from flask_restful import Resource, reqparse
from .repositories import TeamRepository
from src.utils.mongoencoder import MongoEncoder

post_parser = reqparse.RequestParser()
post_parser.add_argument("name", type=str)
post_parser.add_argument("user_id", type=int)

class TeamsResource(Resource):
    def get(self):
        """ Return all teams"""
        teams = TeamRepository().get()
        output = []
        for team in teams:
            d = team.as_dict()
            d['users'] = [link.users.as_dict() for link in team.users]
            output.append(d)
        return output
    
    def post(self):
        """Create a new team with a default user

        Returns:
            _type_: Return the team
        """
        args = post_parser.parse_args()
        t = TeamRepository().create_and_add_user(args['name'],
                                             args['user_id'])
        return t.as_dict(), 201


post_team_resource = reqparse.RequestParser()
post_team_resource.add_argument("user_id", type=int)

class TeamResource(Resource):
    def get(self, team_id:str):
        """Get Team information

        Args:
            team_id (str): Team's Id

        Returns:
            _type_: _description_
        """
        teams = TeamRepository().get(team_id)
        output = []
        for team in teams:
            d = team.as_dict()
            d['users'] = [link.users.as_dict() for link in team.users]
            output.append(d)
        return output, 200
    
    def post(self, team_id:int):
        """Add new user to the team

        Args:
            team_id (int): Team's id
        """
        args = post_team_resource.parse_args()
        link = TeamRepository().add_user_to_team(user_id=args['user_id'],
                                            team_id=team_id,
                                            role="Member")
        return link.as_dict(), 201

    def delete(self, team_id:int):
        """Delete team and all associated links

        Args:
            team_id (int): Team id to delete
        """
        TeamRepository().delete(team_id)
        return '', 204