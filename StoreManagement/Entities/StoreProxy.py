import datetime
from StoreManagement.Entities.StoreAccess import StoreAccess
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from StoreManagement.Entities.Store import Store


class StoreProxy:
    """ invariants:
        @inv
    """

    _realStoreID: int = None
    _realStore: 'Store' = None
    _access: 'StoreAccess' = None

    def proxyCheck(self) -> None:
        if self._realStore is None:
            from StoreManagement.Boundaries.DAOs.StoreDAO import StoreDAO
            dao = StoreDAO()
            self._realStore = dao.get(self._realStoreID)
            self._access = StoreAccess(self._realStore)

    def getRealStoreID(self) -> int:
        return self._realStoreID

    def setRealStoreID(self, newID: int) -> None:
        self._realStoreID = newID

    # Main Store calls
    def changeMaxNoOfProduct(self, max: int) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('changeMaxNoOfProduct'):
            raise PermissionError(self._access)
        else:
            self._realStore.changeMaxNoOfProduct(max)

    def subscribe(self, subcriberID: int) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('subscribe'):
            raise PermissionError(self._access)
        else:
            self._realStore.subscribe(subcriberID)

    def unsubscribe(self, subscriberID: int) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('unsubscribe'):
            raise PermissionError(self._access)
        else:
            self._realStore.unsubscribe(subscriberID)

    def deactivate(self) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('deactivate'):
            raise PermissionError(self._access)
        else:
            self._realStore.deactivate()

    def activate(self) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('activate'):
            raise PermissionError(self._access)
        else:
            self._realStore.activate()

    # helpers and checkers
    def isActive(self) -> bool:
        self.proxyCheck()
        return self._realStore.isActive()

    def hasReachedMaxProducts(self) -> bool:
        self.proxyCheck()
        return self._realStore.hasReachedMaxProducts()

    def hasProducts(self) -> bool:
        self.proxyCheck()
        return self._realStore.hasProducts()

    def hasSubscribtion(self) -> bool:
        self.proxyCheck()
        return self._realStore.hasSubscribtion()

    def hasSubscriber(self, subscriberID: int) -> bool:
        self.proxyCheck()
        return self._realStore.hasSubscriber(subscriberID)

    def getNoOfProducts(self) -> int:
        self.proxyCheck()
        return self._realStore.getNoOfProducts()

    def getNoOfSubscribers(self) -> int:
        self.proxyCheck()
        return self._realStore.getNoOfSubscribers()

    # getters and setters
    def getID(self) -> int:
        self.proxyCheck()
        return self._realStore.getID()

    def setID(self, newID: int) -> None:
        self.proxyCheck()
        self._realStore.setID(newID)

    def getMaxNoOfProducts(self) -> int:
        self.proxyCheck()
        return self._realStore.getMaxNoOfProducts()

    def setMaxNoOfProducts(self, max) -> None:
        self.proxyCheck()
        self._realStore.setMaxNoOfProducts(max)

    def getStatus(self) -> str:
        self.proxyCheck()
        return self._realStore.getStatus()

    def setStatus(self, status) -> None:
        self.proxyCheck()
        self._realStore.setStatus(status)

    def getOwnerID(self) -> int:
        self.proxyCheck()
        return self._realStore.getOwnerID()

    def setOwnerID(self, newID: int) -> None:
        self.proxyCheck()
        self.setOwnerID(newID)

    def getProducts(self) -> []:
        self.proxyCheck()
        return self._realStore.getProducts()

    def setProducts(self, products: []) -> None:
        self.proxyCheck()
        self._realStore.setProducts(products)

    def getSubscriberIDs(self) -> []:
        self.proxyCheck()
        return self._realStore.getSubscriberIDs()

    def setSubscriberIDs(self, IDs: []) -> None:
        self.proxyCheck()
        self._realStore.setSubscriberIDs(IDs)

    def getDate(self) -> datetime.datetime:
        self.proxyCheck()
        return self._realStore.getDate()

    def setDate(self, date: datetime.datetime) -> None:
        self.proxyCheck()
        self._realStore.setDate(date)

