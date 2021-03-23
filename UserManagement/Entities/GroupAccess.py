from UserManagement.Boundaries.CurrentUserService import CurrentUserService
from UserManagement.Entities.UserProxy import UserProxy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from UserManagement.Entities.Group import Group


# import UserManagement.Entities.Group as Group


class GroupAccess:
    _group = None
    _currentUserID: int = None
    _userService: CurrentUserService = None

    def __init__(self, group: 'Group') -> None:
        return
        self._group = group
        self._userService = CurrentUserService()
        self._currentUserID = self._userService.getCurrentUserID()

    def isAccessible(self, operation) -> bool:
        return True

        currentUserID: int = self._currentUserID
        currentUser = UserProxy()
        currentUser.setRealUserID(currentUserID)

        if operation == 'addUser':
            if ownerID == currentUserID:
                return True
            elif currentUser.isStaff() and currentUser.hasGroupPrivilege('write'):
                return True
            else:
                return False

        if operation == 'removeUser':
            if ownerID == currentUserID:
                return True
            elif currentUser.isStaff() and currentUser.hasGroupPrivilege('write'):
                return True
            else:
                return False
