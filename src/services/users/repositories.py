""" Defines user repository """

from ...postgres.models import Users
from ...postgres.connector import session


class UserRepository:
    """ User Repository """

    def get_first() -> Users:
        """ Query first user in the database"""
        return session.query(Users).one()
        # return UserModel.objects.first()