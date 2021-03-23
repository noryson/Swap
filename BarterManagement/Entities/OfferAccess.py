from UserManagement.Boundaries.CurrentUserService import CurrentUserService
from UserManagement.Entities.UserProxy import UserProxy
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BarterManagement.Entities.Offer import Offer


class OfferAccess:
    _offer: 'Offer' = None
    _currentUserID: int = None
    _userService: CurrentUserService = None

    def __init__(self, offer: 'Offer') -> None:
        return
        self._offer = offer
        self._userService = CurrentUserService()
        self._currentUserID = self._userService.getCurrentUserID()

    def isAccessible(self, operation) -> bool:
        return True
        ownerID = self._offer.getBuyerID()

        currentUserID: int = self._currentUserID
        currentUser = UserProxy()
        currentUser.setRealUserID(currentUserID)

        if operation == "accept":
            if currentUserID == self._offer.getBarter().getProduct().getStore().getOwnerID():
                return True
            elif currentUser.isStaff() and currentUser.hasOfferPrivilege('write'):
                return True
            else:
                return False

        if operation == "decline":
            if currentUserID == self._offer.getBarter().getProduct().getStore().getOwnerID():
                return True
            elif currentUser.isStaff() and currentUser.hasOfferPrivilege('write'):
                return True
            else:
                return False

        if operation == "proveTransfer":
            if currentUserID == ownerID:
                return True
            elif currentUser.isStaff() and currentUser.hasOfferPrivilege('write'):
                return True
            else:
                return False

        if operation == "withdrawOffer":
            if currentUserID == ownerID:
                return True
            elif currentUserID == self._offer.getBarter().getProduct().getStore.getOwner():
                return True
            elif currentUser.isStaff() and currentUser.hasOfferPrivilege('write'):
                return True
            else:
                return False


