import datetime
from Exceptions.BarterExceptions import *
from Exceptions.OfferExceptions import *
from Exceptions.ProofExceptions import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BarterManagement.Entities.OfferProxy import OfferProxy
    from BarterManagement.Entities.ProductProxy import ProductProxy


class Barter:
    """ invariants:
        @inv no attributes must be None
        @inv getMaxNoOfOffers() >= 0
        @inv getStatus() = ['concluded', 'running', 'terminated', 'transferring']
        @inv currentDate < endDate
        @inv Product.getBarters() contains self
    """

    _barterID: int = None
    _request: str = None
    _maxNoOfOffers: int = None
    _endDate: datetime.datetime = None
    _status: str = None
    _adminStatus: str = None
    _offers: ['OfferProxy'] = None  # Ghost
    _product: 'ProductProxy' = None  # Ghost

    """ terminate()
        @pre isDeactivated() = False
        @pre isConcluded() = False
        @pre isTerminated() = False
        @pre isTransferring() = False
        @post isTerminated() = True
    """
    def terminate(self) -> None:
        if self.isDeactivated():
            raise BarterDeactivatedException(self.getID())
        if self.isConcluded():
            raise BarterConcludedException(self.getID())
        if self.isTerminated():
            raise BarterTerminatedException(self.getID())
        if self.isTransferring():
            raise BarterTransferringException(self.getID())

        self.setStatus('terminated')
        self.synchronizeDB()

    """ conclude()
        @pre isConcluded() = False
        @pre isTerminated() = False
        @pre isTransferring() = True
        @pre offer.proof.isConfirmed() = True
        @post isConcluded() = True
    """
    def conclude(self) -> None:
        if self.isDeactivated():
            raise BarterDeactivatedException(self.getID())
        if self.isConcluded():
            raise BarterConcludedException(self.getID())
        if self.isTerminated():
            raise BarterTerminatedException(self.getID())
        if not self.isTransferring():
            raise BarterHasNoOfferException(self.getID())

        for offer in self.getOffers():  # find accepted offer and determine if it doesn't have a proof
            if offer.isAccepted():
                if not offer.hasProof():
                    raise OfferHasNoProofException(offer.getID())

                for proof in offer.getProofs():
                    if not proof.isConfirmed():
                        raise ProofNotConfirmedException(proof.getID())

                self.setStatus('concluded')
                self.synchronizeDB()
                return

    """ beginTransaction()
        @pre isConcluded() = False
        @pre isTerminated() = False
        @pre isTransferring() = False
        @pre hasAcceptance() = True
    """
    def beginTransfer(self) -> None:
        if self.isDeactivated():
            raise BarterDeactivatedException(self.getID())
        if self.isConcluded():
            raise BarterConcludedException(self.getID())
        if self.isTerminated():
            raise BarterTerminatedException(self.getID())
        if self.isTransferring():
            raise BarterTransferringException(self.getID())
        if not self.hasAcceptance():
            raise BarterHasNoAcceptanceException(self.getID())

        self.setStatus('transferring')
        self.synchronizeDB()

    """ endTransfer()
        @pre isConcluded() = False
        @pre isTransferring() = True
        @pre isTerminated() = False
        @pre offers.hasProof() = False
    """
    def endTransfer(self) -> None:
        if self.isDeactivated():
            raise BarterDeactivatedException(self.getID())
        if self.isConcluded():
            raise BarterConcludedException(self.getID())
        if self.isTerminated():
            raise BarterTerminatedException(self.getID())
        if not self.isTransferring():
            raise BarterNotTransferringException(self.getID())

        for offer in self.getOffers():
            if offer.hasProof():
                raise BarterHasProofException(self.getID())
        self.setStatus('running')
        self.synchronizeDB()

    """ extend()
        @pre isConcluded() = False
        @pre isTerminated() = False
        @pre isTransferring() = False
    """
    def extend(self, day: datetime.datetime) -> None:
        if self.isDeactivated():
            raise BarterDeactivatedException(self.getID())
        if self.isConcluded():
            raise BarterConcludedException(self.getID())
        if self.isTerminated():
            raise BarterTerminatedException(self.getID())
        if self.isTransferring():
            raise BarterTransferringException(self.getID())

        self._endDate += day
        self.synchronizeDB()

    """ deactivate()
        @pre isActive() == True
    """
    def deactivate(self) -> None:
        if self.isActive():
            self._adminStatus = 'deactivated'
            self.synchronizeDB()

    """ Activate()
        @pre isDeactivated() == True
    """
    def activate(self) -> None:
        if self.isDeactivated():
            self._adminStatus = 'activate'
            self.synchronizeDB()

    # checkers and helpers
    def isDeactivated(self) -> bool:
        if self.getAdminStatus() == "deactivated":
            return True
        return False

    def isActive(self) -> bool:
        if self.getAdminStatus() == "active":
            return True
        return False

    def isConcluded(self) -> bool:
        if self.getStatus() == "concluded":
            return True
        return False

    def isTerminated(self) -> bool:
        if self.getStatus().lower() == "terminated":
            return True
        return False

    def isRunning(self) -> bool:
        if self.getStatus() == "running" or self.getStatus() == 'transferring':
            return True
        return False

    def isTransferring(self) -> bool:
        if self.getStatus() == "transferring":
            return True
        return False

    def hasAcceptance(self) -> bool:
        for offer in self.getOffers():
            if offer.isAccepted():
                return True
        return False

    def getNoOfOffers(self) -> int:
        return len(self.getOffers())

    def synchronizeDB(self) -> None:
        from BarterManagement.Boundaries.BarterDAO import BarterDAO

        dao: BarterDAO = BarterDAO()
        dao.update(self)

    # getters and setters
    def getRequest(self) -> str:
        return self._request

    def setRequest(self, newRequest: str) -> None:
        self._request = newRequest

    def getMaxNoOfOffers(self) -> int:
        return self._maxNoOfOffers

    def setMaxNoOfOffers(self, newMax: int) -> None:
        self._maxNoOfOffers = newMax

    def getEndDate(self) -> datetime:
        return self._endDate

    def setEndDate(self, newDate: datetime.datetime) -> None:
        self._endDate = newDate

    def getStatus(self) -> str:
        return self._status

    def setStatus(self, newStatus: str) -> None:
        self._status = newStatus

    def getAdminStatus(self) -> str:
        return self._adminStatus

    def setAdminStatus(self, newStatus: str) -> None:
        self._adminStatus = newStatus

    def getID(self) -> int:
        return self._barterID

    def setID(self, newBarterID: int) -> None:
        self._barterID = newBarterID

    def getOffers(self) -> []:
        return self._offers

    def setOffers(self, offers: ['OfferProxy']) -> None:
        self._offers = offers

    def getProduct(self) -> 'ProductProxy':
        return self._product

    def setProduct(self, newProduct: 'ProductProxy') -> None:
        self._product = newProduct
