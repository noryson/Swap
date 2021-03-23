import datetime
from BarterManagement.Entities.OfferAccess import OfferAccess
from Exceptions.OfferExceptions import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BarterManagement.Entities.Offer import Offer
    from BarterManagement.Entities.BarterProxy import BarterProxy
    from BarterManagement.Entities.ProofProxy import ProofProxy
    from UserManagement.Entities.UserProxy import UserProxy


class OfferProxy:
    """ invariants:
        @inv
    """

    _realOffer: 'Offer' = None
    _realOfferID: int = None
    _access: OfferAccess = None

    # OfferProxy calls
    def proxyCheck(self) -> None:
        if self._realOffer is None:
            try:
                from BarterManagement.Boundaries.OfferDAO import OfferDAO
                offerDao = OfferDAO()
                self._realOffer = offerDao.get(self._realOfferID)
                self._access = OfferAccess(self._realOffer)
            except OfferNotFoundException(self):
                pass

    def getRealOfferID(self) -> int:
        return self._realOfferID

    def setRealOfferID(self, newID: int) -> None:
        self._realOfferID = newID

    # main Offer calls
    def accept(self) -> None:
        self.proxyCheck()
        if not self._access.isAccessible("accept"):
            raise PermissionError(self._access)
        else:
            self._realOffer.accept()

    def decline(self) -> None:
        self.proxyCheck()
        if not self._access.isAccessible("decline"):
            raise PermissionError(self._access)
        else:
            self._realOffer.decline()

    # checkers and helpers
    def isAccepted(self) -> bool:
        self.proxyCheck()
        return self._realOffer.isAccepted()

    def hasProof(self) -> bool:
        self.proxyCheck()
        return self._realOffer.hasProof()

    def getNoOfProofs(self) -> int:
        self.proxyCheck()
        return self._realOffer.getNoOfProofs()

    # getters and setters
    def getOfferedProduct(self) -> str:
        self.proxyCheck()
        return self._realOffer.getOfferedProduct()

    def setOfferedProduct(self, newProduct: str) -> None:
        self.proxyCheck()
        self._realOffer.setOfferedProduct(newProduct)

    def getStatus(self) -> str:
        self.proxyCheck()
        return self._realOffer.getStatus()

    def setStatus(self, newStatus: str) -> None:
        self.proxyCheck()
        self._realOffer.setStatus(newStatus)

    def getID(self) -> int:
        self.proxyCheck()
        return self._realOffer.getID()

    def setID(self, newID: int) -> None:
        self.proxyCheck()
        self._realOffer.setID(newID)

    def getDate(self) -> datetime:
        self.proxyCheck()
        return self._realOffer.getDate()

    def setDate(self, newDate: datetime.datetime) -> None:
        self.proxyCheck()
        self._realOffer.setDate(newDate)

    def getBarter(self) -> 'BarterProxy':
        self.proxyCheck()
        return self._realOffer.getBarter()

    def setBarter(self, newBarter: 'BarterProxy') -> None:
        self.proxyCheck()
        self._realOffer.setBarter(newBarter)

    def getBuyer(self) -> 'UserProxy':
        self.proxyCheck()
        return self._realOffer.getBuyer()

    def setBuyer(self, newBuyer: 'UserProxy') -> None:
        self.proxyCheck()
        self._realOffer.setBuyer(newBuyer)

    def getProofs(self) -> []:
        self.proxyCheck()
        return self._realOffer.getProofs()

    def setProofs(self, newProofs: []) -> None:
        self.proxyCheck()
        self._realOffer.setProofs(newProofs)



