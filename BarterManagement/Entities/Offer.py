import datetime
import sys

m = 'BarterManagement.Entities.BarterProxy'
if m not in sys.modules:
    from BarterManagement.Entities.BarterProxy import BarterProxy
else:
    BarterProxy = sys.modules['BarterManagement.Entities.BarterProxy']
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BarterManagement.Entities.BarterProxy import BarterProxy
    from BarterManagement.Entities.ProofProxy import ProofProxy
    from UserManagement.Entities.UserProxy import UserProxy
from Exceptions.BarterExceptions import *
from Exceptions.OfferExceptions import *
# from Exceptions.ProofExceptions import *


class Offer:
    """ invariants:
        @inv all fields should be filled
        @inv getStatus() = ['accepted', 'unaccepted']
        @inv barter.is[deactivated, terminated] == False
    """
    _offerID: int = None
    _offeredProduct: str = None
    _status: str = None
    _creationDate: datetime.datetime = None
    _buyer: 'UserProxy' = None
    _barter: 'BarterProxy' = None
    _proofs: ['ProofProxy'] = None

    """ acceptOffer(offer):void
        @pre offerDTO.owner !contains getOffers().owners
        @pre getAcceptedOffer() = None
        @pre isConcluded() = False
        @pre isTransferring = False
        @pre isAccepted() = False
        @post isTransferring = True
        @post isAccepted = True
        @post getAcceptedOffer() = offer
    """
    def accept(self):
        barter: BarterProxy = self.getBarter()
        if barter.isDeactivated():
            raise BarterDeactivatedException(barter.getID())
        if barter.isConcluded():
            raise BarterConcludedException(barter.getID())
        if barter.isTerminated():
            raise BarterTerminatedException(barter.getID())
        if barter.isTransferring():
            raise BarterTransferringException(barter.getID())
        if self.isAccepted():
            raise OfferIsAcceptedException(self)

        # The code below should be handled at the Proxy
        # for offer in self.getBarter().getOffers():
        #     if offer.getBuyerID == self.getBuyer().getID():
        #         raise PermissionError("Access denied.")

        self.setStatus('accepted')
        self.synchronizeDB()
        barter.beginTransfer()

    """ rejectOffer(offer):void
        @pre getAcceptedOffer() = offer
        @pre isConcluded() = False
        @pre isTransferring() = True
        @pre hasProof() = False
        @post getAcceptedOffer() = None
        @post isTransferring = False
    """
    def decline(self):
        if self.getBarter().isDeactivated():
            raise BarterDeactivatedException(self.getBarter().getID())
        if self.getBarter().isConcluded():
            raise BarterConcludedException(self.getBarter().getID())
        if self.getBarter().isTerminated():
            raise BarterTerminatedException(self.getBarter().getID())
        if not self.getBarter().hasAcceptance():
            raise BarterHasNoAcceptanceException(self.getBarter().getID())
        if not self.isAccepted():
            raise OfferNotAcceptedException(self)
        if self.hasProof():
            raise OfferHasProofException(self.getID())

        # This should be handled in a proxy
        # for offer in self.getBarter().getOffers():
        #     if offer.getBuyerID == self.getBuyer().getID():
        #         raise PermissionError("Access denied.")

        self.setStatus("unaccepted")
        self.synchronizeDB()
        self.getBarter().endTransfer()

    # checkers and helpers
    def isAccepted(self) -> bool:
        # print(self.getStatus())
        if self.getStatus() == "accepted":
            return True
        else:
            return False

    def hasProof(self) -> bool:
        if len(self.getProofs()) > 0:
            return True
        else:
            return False

    def getNoOfProofs(self) -> int:
        return len(self.getProofs())

    def synchronizeDB(self) -> None:
        from BarterManagement.Boundaries.OfferDAO import OfferDAO

        dao: OfferDAO = OfferDAO()
        dao.update(self)

    # getters and setters
    def getOfferedProduct(self) -> str:
        return self._offeredProduct

    def setOfferedProduct(self, newProduct: str) -> None:
        self._offeredProduct = newProduct

    def getStatus(self) -> str:
        return self._status

    def setStatus(self, newStatus: str) -> None:
        self._status = newStatus

    def getID(self) -> int:
        return self._offerID

    def setID(self, newID: int) -> None:
        self._offerID = newID

    def getDate(self) -> datetime:
        return self._creationDate

    def setDate(self, newDate: datetime.datetime) -> None:
        self._creationDate = newDate

    def getBarter(self) -> BarterProxy:
        return self._barter

    def setBarter(self, newBarter: BarterProxy) -> None:
        self._barter = newBarter

    def getBuyer(self) -> 'UserProxy':
        return self._buyer

    def setBuyer(self, newBuyer: 'UserProxy') -> None:
        self._buyer = newBuyer

    def getProofs(self) -> []:
        return self._proofs

    def setProofs(self, newProofs: ['ProofProxy']) -> None:
        self._proofs = newProofs