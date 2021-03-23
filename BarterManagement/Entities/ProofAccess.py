from UserManagement.Boundaries.CurrentUserService import CurrentUserService
from BarterManagement.Entities.Proof import Proof
from UserManagement.Entities.UserProxy import UserProxy


class ProofAccess:
    _proof: Proof = None
    _currentUserID: int = None
    _userService: CurrentUserService = None

    def __init__(self, proof: Proof) -> None:
        return
        self._proof = proof
        self._userService = CurrentUserService()
        self._currentUserID = self._userService.getCurrentUserID()

    def isAccessible(self, operation):
        return True
        sellerID: int = self._proof.getOffer().getBarter().getProduct().getStore().getOwnerID()
        buyerID: int = self._proof.getOffer().getBuyerID()
        ownerID: int = self._proof.getOwnerID()
        currentUserID: int = self._currentUserID

        currentUserID: int = self._currentUserID
        currentUser = UserProxy()
        currentUser.setRealUserID(currentUserID)

        if operation == 'confirm' or operation == 'deny':
            checkID: int = None
            if ownerID == sellerID:
                checkID = buyerID
            else:
                checkID = sellerID

            if currentUserID == checkID:
                return True
            elif currentUser.isStaff() and currentUser.hasProofPrivilege('write'):
                return True
            else:
                return False

        if operation == "delete":
            if userService.isCurrentUser(ownerID):
                return True
            elif userService.isStaff() and currentUser.hasProofPrivilege('write'):
                return True
            else:
                return False