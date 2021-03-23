from UserManagement.Entities.UserProxy import UserProxy
from Exceptions.UserExceptions import *


class DisplayUserControl:
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
        return self._user

