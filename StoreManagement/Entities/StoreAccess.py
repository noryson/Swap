from UserManagement.Boundaries.CurrentUserService import CurrentUserService
from UserManagement.Entities.UserProxy import UserProxy
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from StoreManagement.Entities.Store import Store


class StoreAccess:
    _store: Store = None
    _currentUserID: int = None
    _userService: CurrentUserService = None

    def __init__(self, store: Store) -> None:
        self._store = store
        self._userService = CurrentUserService()
        self._currentUserID = self._userService.getCurrentUserID()

    def isAccessible(self, operation) -> bool:
        ownerID: int = self._store.getOwnerID()
        
        currentUserID: int = self._currentUserID
        currentUser = UserProxy()
        currentUser.setRealUserID(currentUserID)

        if operation == 'changeMaxNoOfProduct':
            if currentUser.isStaff() and currentUser.hasStorePrivilege('write'):
                return True
            else:
                return False

        if operation == 'subscribe':
            if currentUserID == ownerID:
                return False
            elif not currentUser.isActive():
                return False
            else:
                return True

        if operation == 'unsubscribe':
            if currentUserID == ownerID:
                return False
            elif not currentUser.isActive():
                return False
            else:
                return True

        if operation == 'deactivate':
            if currentUser.isStaff() and currentUser.hasStorePrivilege('write'):
                return True
            else:
                return False

        if operation == 'activate':
            if currentUser.isStaff() and currentUser.hasStorePrivilege('write'):
                return True
            else:
                return False
