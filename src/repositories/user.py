""" Defines user repository """

from ..grql.models import UserModel

class UserRepository:
    """ User Repository """

    def get_first() -> UserModel:
        """ Query first user in the database"""
        return UserModel.objects.first()