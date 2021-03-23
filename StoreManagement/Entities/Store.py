import datetime
from Exceptions.StoreExceptions import *


class Store:
    """
        @inv isActive = True
        @invariant maxNumberOfProducts >= 0
        @invariant owner = getAllProducts().store.owner
        @invariant getNumberOfProducts() <= getMaxNumberOfProducts()
        @invariant storeID, owner, status != None
        @inv getStatus() = ['active', 'deactivated']
    """
    _storeID: int = None
    _maxNoOfProducts: int = None
    _status: str = None
    _ownerID: int = None
    _products: [] = list()
    _subscriberIDs: [] = list()
    _creationDate: datetime.datetime = None

    """ changeMaxNoOfProduct()
        @pre isActive() = True
        @post MaxNoOfProduct = max
    """
    def changeMaxNoOfProduct(self, maxNoOfProducts) -> None:
        if maxNoOfProducts <= 0:
            raise ValueError('invalid max no')
        if not self.isActive():
            raise StoreIsDeactivatedException(self)

        self.setMaxNoOfProducts(max)
        self.synchronizeDB()

    """ subscribe(subscriberID)
        @pre getSubscriberIDs !contain subscriberID
        @post getSubscriberIDs contain subscriberID
    """
    def subscribe(self, subscriberID: int):
        if not self.isActive():
            raise StoreIsDeactivatedException(self)

        if self.hasSubscriber(subscriberID):
            raise StoreSubscriberExistException(self, subscriberID)

        self._subscriberIDs.append(subscriberID)
        self.synchronizeDB()

    """ subscribe(subscriberID)
        @pre getSubscriberIDs contain subscriberID
        @post getSubscriberIDs !contain subscriberID
    """
    def unsubscribe(self, subscriberID: int):
        if not self.isActive():
            raise StoreIsDeactivatedException(self)

        if self.hasSubscriber(subscriberID):
            raise StoreSubscriberNonExistentException(self, subscriberID)

        inc: int = 0
        for subID in self.getSubscriberIDs():
            if subscriberID == subID:
                self._subscriberIDs.pop(inc)
            inc += 1
        self.synchronizeDB()

    """ deactivated()
        @pre isActivated()
        @post !isActivated()
    """
    def deactivate(self):
        if not self.isActive():
            raise StoreIsDeactivatedException(self)
        self.setStatus('deactivated')
        self.synchronizeDB()

    """ activate()
        @pre !isActivated()
        @post isActivated()
    """
    def activate(self):
        if self.isActive():
            raise StoreIsActiveException(self)
        self.setStatus('active')
        self.synchronizeDB()

    # helpers and checkers
    def isActive(self) -> bool:
        if self.getStatus() == 'active':
            return True
        else:
            return False

    def calculateStatistics(self):
        pass

    def hasReachedMaxProducts(self) -> bool:
        if self.getNoOfProducts() >= self.getMaxNoOfProducts():
            return True
        else:
            return False

    def hasProducts(self) -> bool:
        if self.getNoOfProducts() > 0:
            return True
        else:
            return False

    def hasSubscribtion(self) -> bool:
        if self.getNoOfSubscribers() > 0:
            return True
        else:
            return False

    def hasSubscriber(self, subscriberID: int) -> bool:
        for subID in self.getSubscriberIDs():
            if subscriberID == subID:
                return True
        return False

    def getNoOfProducts(self) -> int:
        return len(self.getProducts())

    def getNoOfSubscribers(self) -> int:
        return len(self.getSubscriberIDs())

    def synchronizeDB(self) -> None:
        from StoreManagement.Boundaries.DAOs.StoreDAO import StoreDAO
        dao = StoreDAO()
        dao.update(self)

    # getters and setters
    def getID(self) -> int:
        return self._storeID

    def setID(self, newID: int) -> None:
        self._storeID = newID

    def getMaxNoOfProducts(self) -> int:
        return self._maxNoOfProducts

    def setMaxNoOfProducts(self, max) -> None:
        self._maxNoOfProducts = max

    def getStatus(self) -> str:
        return self._status

    def setStatus(self, status) -> None:
        self._status: str = status

    def getOwnerID(self) -> int:
        return self._ownerID

    def setOwnerID(self, newID: int) -> None:
        self._ownerID = newID

    def getProducts(self) -> []:
        return self._products

    def setProducts(self, products: []) -> None:
        self._products: [] = products

    def getSubscriberIDs(self) -> []:
        return self._subscriberIDs

    def setSubscriberIDs(self, IDs: []) -> None:
        self._subscriberIDs: [] = IDs

    def getDate(self) -> datetime.datetime:
        return self._creationDate

    def setDate(self, date: datetime.datetime) -> None:
        self._creationDate = date

