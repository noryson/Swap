from UserManagement.Entities.UserProxy import UserProxy
from Exceptions.UserExceptions import *


class ChangeUserPasswordControl:
    _user: UserProxy = None
    _secret: str = None

    def __init__(self, userID: int, secret: str) -> None:
        try:
            user: UserProxy = UserProxy()
            user.setID(userID)
            user.proxyCheck
        except UserNotFoundException:
            raise RuntimeError(userID)

        self._user = user
        self._secret = secret
        # self.setUser(user)

    def execute(self) -> None:
        try:
            self._user.changeSecret(self._secret)
        except PermissionError:
            raise RuntimeError('Access denied')

