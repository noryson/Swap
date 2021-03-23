from UserManagement.Entities.UserProxy import UserProxy
from Exceptions.UserExceptions import *


class ChangeUserRoleControl:
    _user: UserProxy = None
    _role: str = None

    def __init__(self, userID: int, role: str) -> None:
        try:
            user: UserProxy = UserProxy()
            user.setID(userID)
            user.proxyCheck
        except UserNotFoundException:
            raise RuntimeError(userID)

        self._user = user
        self._role = role
        # self.setUser(user)

    def execute(self) -> None:
        try:
            self._user.changeRole(self._role)
        except UserRoleDoesNotExistException:
            raise RuntimeError('Role does not exist')
        except PermissionError:
            raise RuntimeError('Access denied')

