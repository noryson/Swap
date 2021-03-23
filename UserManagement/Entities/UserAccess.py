from UserManagement.Boundaries.CurrentUserService import CurrentUserService
from UserManagement.Entities.UserProxy import UserProxy
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from UserManagement.Entities.User import User
# import UserManagement.Entities.User as User


class UserAccess:
    _user = None
    _currentUserID: int = None
    _userService: CurrentUserService = None

    def __init__(self, user: 'User') -> None:
        return
        self._user = user
        self._userService = CurrentUserService()
        self._currentUserID = self._userService.getCurrentUserID()

    def isAccessible(self, operation) -> bool:
        return True
        userService: CurrentUserService = self._userService
        ownerID: int = self._user.getID()

        currentUserID: int = self._currentUserID
        currentUser = UserProxy()
        currentUser.setRealUserID(currentUserID)

        if operation == 'login':
            if ownerID == currentUserID:
                return True
            else:
                return False

        if operation == 'logout':
            if ownerID == currentUserID:
                return True
            else:
                return False

        if operation == 'changeSecret':
            if ownerID == currentUserID:
                return True
            elif currentUser.isStaff() and currentUser.hasUserPrivilege('write'):
                return True
            else:
                return False

        if operation == 'changeProfileImage':
            if ownerID == currentUserID:
                return True
            elif currentUser.isStaff() and currentUser.hasUserPrivilege('write'):
                return True
            else:
                return False

        if operation == 'changeRole':
            if currentUser.isStaff() and currentUser.hasUserPrivilege('write'):
                return True
            else:
                return False

        if operation == 'deactivate':
            if currentUser.isStaff() and currentUser.hasUserPrivilege('write'):
                return True
            else:
                return False

        if operation == 'activate':
            if currentUser.isStaff() and currentUser.hasUserPrivilege('write'):
                return True
            else:
                return False

        if operation == 'updateLastLogin':
            if ownerID == currentUserID:
                return True
            elif currentUser.isStaff() and currentUser.hasUserPrivilege('write'):
                return True
            else:
                return False



            