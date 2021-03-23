import datetime
from BarterManagement.Entities.BarterAccess import BarterAccess
from Exceptions.BarterExceptions import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BarterManagement.Entities.Barter import Barter
    from BarterManagement.Entities.OfferProxy import OfferProxy
    from BarterManagement.Entities.ProductProxy import ProductProxy
#from BarterManagement.Entities.Barter import Barter

class BarterProxy:
    """ invariants:
        @inv no value = None
    """

    _realBarterID: int = None
    _realBarter: 'Barter' = None
    _access: 'BarterAccess' = None

    # BarterProxy calls
    def proxyCheck(self) -> None:
        if self._realBarter is None:
            from BarterManagement.Boundaries.BarterDAO import BarterDAO
            barterDao = BarterDAO()
            self._realBarter = barterDao.get(self._realBarterID)
            self._access = BarterAccess(self._realBarter)

    def getRealBarterID(self) -> int:
        return self._realBarterID

    def setRealBarterID(self, newID: int) -> None:
        self._realBarterID = newID

    # main Barter calls
    def terminate(self) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('terminate'):
            raise PermissionError(self._access)
        else:
            self._realBarter.terminate()

    def conclude(self) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('conclude'):
            raise PermissionError(self._access)
        else:
            self._realBarter.conclude()

    def beginTransfer(self) -> None:
        self.proxyCheck()
        self._realBarter.beginTransfer()

    def endTransfer(self) -> None:
        self.proxyCheck()
        self._realBarter.endTransfer()

    def extend(self, day: datetime) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('extend'):
            raise PermissionError(self._access)
        else:
            self._realBarter.extend(day)

    def deactivate(self) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('deactivate'):
            raise PermissionError(self._access)
        else:
            self._realBarter.deactivate()

    def activate(self) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('activate'):
            raise PermissionError(self._access)
        else:
            self._realBarter.activate()

    # checkers and helpers
    def isDeactivated(self) -> bool:
        self.proxyCheck()
        return self._realBarter.isDeactivated()

    def isActive(self) -> bool:
        self.proxyCheck()
        return self._realBarter.isActive()

    def isConcluded(self) -> bool:
        self.proxyCheck()
        return self._realBarter.isConcluded()

    def isTerminated(self) -> bool:
        self.proxyCheck()
        return self._realBarter.isTerminated()

    def isRunning(self) -> bool:
        self.proxyCheck()
        return self._realBarter.isRunning()

    def isTransferring(self) -> bool:
        self.proxyCheck()
        return self._realBarter.isTransferring()

    def hasAcceptance(self) -> bool:
        self.proxyCheck()
        return self._realBarter.hasAcceptance()

    def getNoOfOffers(self) -> int:
        self.proxyCheck()
        return self._realBarter.getNoOfOffers()

    # getters and setters
    def getRequest(self) -> str:
        self.proxyCheck()
        return self._realBarter.getRequest()

    def setRequest(self, newRequest: str) -> None:
        self.proxyCheck()
        self._realBarter.setRequest(newRequest)

    def getMaxNoOfOffers(self) -> int:
        self.proxyCheck()
        return self._realBarter.getMaxNoOfOffers()

    def setMaxNoOfOffers(self, newMax: int) -> None:
        self.proxyCheck()
        self._realBarter.setMaxNoOfOffers(newMax)

    def getEndDate(self) -> datetime:
        self.proxyCheck()
        return self._realBarter.getEndDate()

    def setEndDate(self, newDate: datetime) -> None:
        self.proxyCheck()
        self._realBarter.setEndDate(newDate)

    def getStatus(self) -> str:
        self.proxyCheck()
        return self._realBarter.getStatus()

    def setStatus(self, newStatus: str) -> None:
        self.proxyCheck()
        self._realBarter.setStatus(newStatus)

    def getAdminStatus(self) -> str:
        self.proxyCheck()
        return self._realBarter.getAdminStatus()

    def setAdminStatus(self, newStatus: str) -> None:
        self.proxyCheck()
        self._realBarter.setAdminStatus(newStatus)

    def getID(self) -> int:
        self.proxyCheck()
        return self._realBarter.getID()

    def setID(self, newBarterID: int) -> None:
        self.proxyCheck()
        self._realBarter.setID(newBarterID)

    def getOffers(self) -> []:  # Ghost
        self.proxyCheck()
        return self._realBarter.getOffers()

    def setOffers(self, offers: []) -> None:
        self.proxyCheck()
        self._realBarter.setOffers(offers)

    def getProduct(self) -> 'ProductProxy':
        self.proxyCheck()
        return self._realBarter.getProduct()

    def setProduct(self, newProduct: 'ProductProxy') -> None:
        self.proxyCheck()
        self._realBarter.setProduct(newProduct)

