from UserManagement.Boundaries.CurrentUserService import CurrentUserService
from UserManagement.Entities.UserProxy import UserProxy
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BarterManagement.Entities.Barter import Barter
# import BarterManagement.Entities.Barter as Barter


class BarterAccess:
    _barter = None
    _currentUserID: int = None
    _userService: CurrentUserService = None

    def __init__(self, barter: 'Barter') -> None:
        return
        self._barter = barter
        self._userService = CurrentUserService()
        self._currentUserID = self._userService.getCurrentUserID()

    def isAccessible(self, operation) -> bool:
        return True
        userService: CurrentUserService = self._userService
        currentUser = UserProxy()
        ownerID: int = self._barter.getProduct().getStore().getOwnerID()
        currentUserID: int = self._currentUserID
        currentUser.setRealUserID(currentUserID)

        if operation == 'terminate':
            if ownerID == currentUserID:
                return True
            elif currentUser.isStaff() and currentUser.hasBarterPrivilege('write'):
                return True
            else:
                return False

        if operation == 'conclude':
            if ownerID == currentUserID:
                return True
            elif currentUser.isStaff() and currentUser.hasBarterPrivilege('write'):
                return True
            else:
                return False

        if operation == 'beginTransfer':
            if ownerID == currentUserID:
                return True

            for offer in self._barter.getOffers():
                if currentUserID == offer.getBuyer().getID():
                    return True

            return False

        if operation == 'extend':
            if ownerID == currentUserID:
                return True
            elif currentUser.isStaff() and currentUser.hasBarterPrivilege('write'):
                return True
            else:
                return False

        if operation == 'deactivate':
            if currentUser.isStaff() and currentUser.hasBarterPrivilege('write'):
                return True
            else:
                return False

        if operation == 'activate':
            if currentUser.isStaff() and currentUser.hasBarterPrivilege('write'):
                return True
            else:
                return False

        if operation == 'withdrawOffer':
            if ownerID == currentUserID:
                return True
            else:
                return False
