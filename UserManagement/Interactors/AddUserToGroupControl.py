from UserManagement.Entities.UserProxy import UserProxy
from UserManagement.Entities.GroupProxy import GroupProxy
from UserManagement.Entities.GroupAccess import GroupAccess
from Exceptions.GroupExceptions import *
from Exceptions.UserExceptions import UserNotFoundException


class AddUserToGroupControl:
    _group: GroupProxy = None
    _user: UserProxy = None

    def __init__(self, groupID: int, userID: int) -> None:
        try:
            group: GroupProxy = GroupProxy()
            group.setID(groupID)
            group.proxyCheck()
            
            user: UserProxy = UserProxy()
            user.setID(userID)
            user.proxyCheck()
        except GroupNotFoundException(groupID):
            raise RuntimeError('group does not exist')
        except UserNotFoundException(userID):
            raise RuntimeError('User does not exist')

        self._group = group
        self._user = user

    def execute(self) -> None:
        try:
            self._group.addUser(self._user)
        except GroupContainsUserException(self._user):
            raise RuntimeError('User already in group')
        except PermissionError:
            raise RuntimeError('Access denied.')

