from UserManagement.Boundaries.CurrentUserService import CurrentUserService
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from StoreManagement.Entities.Category import Category
from UserManagement.Entities.UserProxy import UserProxy


class CategoryAccess:
    _category: Category = None
    _currentUserID: int = None
    _userService: CurrentUserService = None

    def __init__(self, category: Category):
        self._category = category
        self._userService = CurrentUserService()
        self._currentUserID = self._userService.getCurrentUserID()

    def isAccessible(self, operation) -> bool:
        currentUserID: int = self._currentUserID
        currentUser = UserProxy()
        currentUser.setRealUserID(currentUserID)

        if operation == "changeName" or operation == 'delete':
            if currentUser.isStaff() and currentUser.hasCategoryPrivilege('write'):
                return True
            else:
                return False
