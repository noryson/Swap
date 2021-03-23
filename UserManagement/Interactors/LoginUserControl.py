from UserManagement.Entities.UserProxy import UserProxy
from Exceptions.UserExceptions import *


class LoginUserControl:
    _user: UserProxy = None

    def __init__(self, userID: int) -> None:
        try:
            user: UserProxy = UserProxy()
            user.setID(userID)
            user.proxyCheck
        except UserNotFoundException:
            raise RuntimeError(userID)

        self._user = user
        # self.setUser(user)

    def execute(self) -> None:
        try:
            self._user.login()
        except UserIsOnlineException:
            raise RuntimeError('User is already online')
        except PermissionError:
            raise RuntimeError('Access denied')

