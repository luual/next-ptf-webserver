""" Defines team repository """

from ...postgres.models import Teams, Users_Teams, Users
from ...postgres.connector import session

from sqlalchemy import select, insert


class TeamRepository:
    """ User Repository """

    def create(self, team_name:str) -> Teams:
        '''Create a new team'''
        team = Teams(name=team_name)
        session.add(team)
        session.commit()
        return team

    def get(self, id:int = None ) -> list["Teams"]:
        """Retrieve Team or Teams

        Args:
            id (int): team's id to search
        Returns:
            list[Teams]: list of Teams
        """
        if id is None:
            return session.query(Teams).all()
        return session.query(Teams).filter(Teams.id==id).all()
        

    def delete(self, id: int) -> None:
        """Delete a team and all associated links

        Args:
            id (int): Team's id to delete
        """
        session.query(Users_Teams).filter(Users_Teams.teams_id==id).delete()
        session.query(Teams).filter(Teams.id==id).delete()
        session.commit()

    def create_and_add_user(self, team_name:str, user_id:int) -> Teams:
        """Create a new team with an user

        Args:
            team_name (str): team name
            user_id (int): user id as owner
        """
        new_team = Teams(name=team_name)
        session.add(new_team)
        session.flush() # Push the team to the database and create autogeneration
        link = Users_Teams(teams_id=new_team.id, users_id=user_id, role="Admin")
        session.add(link)
        session.commit()
        return new_team

    def update_name(self, id: int, team_name:str) -> Teams:
        """Update the team name

        Args:
            id (int): team's id
            team_name (str): new team name

        Returns:
            Teams: Updated Team
        """
        team = session.query(Teams).filter(Teams.id==id).one()
        team.name = team_name
        session.commit()
        return team

    def add_user_to_team(self, user_id: int,team_id, role:str) -> Users_Teams:
        """Add existing user to an existing team

        Args:
            user_id (int): User id
            team_id (_type_): Team id
            role (str): Associated role for user
        """
        user_link = Users_Teams(users_id=user_id, teams_id=team_id, role=role)
        session.add(user_link)
        session.commit()
        return user_link

    def remove_user_from_team(self, user_id: int, team_id:int) -> None:
        '''
        Remove specific user from a team
        '''
        session.query(Users_Teams) \
        .filter(Users_Teams.teams_id==team_id and Users_Teams.users_id==user_id) \
        .delete()
        
        session.commit()

    def update_role(self, user_id:int, team_id:int, role:str) -> None:
        '''
        Update user role inside specific team
        '''
        link = session.query(Users_Teams) \
        .filter(Users_Teams.teams_id==team_id and Users_Teams.users_id==user_id) \
        .one()

        link.role = role
        session.commit()
        return link