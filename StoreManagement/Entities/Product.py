import datetime
from StoreManagement.Entities.StoreProxy import StoreProxy
from StoreManagement.Entities.CategoryProxy import CategoryProxy
from Exceptions.StoreExceptions import StoreIsDeactivatedException
from Exceptions.ProductExceptions import ProductIsSwappedException


class Product:
    """ @inv store.isActive() = True
        @invariant owner = store.owner
        @invariant getProductImages(), getName(), getDescription(), getOwnerRequest(), getCurrentLocation(),
                    getCreationDate(), getCategory(), getProductID(), getOwner(), getStore() != None
    """
    _productID: int = None
    _name: str = None
    _description: str = None
    _currentLocation: str = None
    _creationDate: datetime.datetime = None
    _category: CategoryProxy = None
    _store: StoreProxy = None
    _imageIDs: [] = list()
    _barterIDs: [] = list

    """" changeLocation(location)
        @pre isSwapped() = False
        @post currentLocation = location
    """
    def changeLocation(self, location: str) -> None:
        if not self.getStore().isActive():
            raise StoreIsDeactivatedException(self.getStore())

        if self.isSwapped():
            raise ProductIsSwappedException(self)

        self.setLocation(location)
        self.synchronizeDB()

    # helpers and checkers
    def calculateStatistics(self) -> {}:
        pass

    def isSwapped(self) -> bool:
        pass  # Implement a BarterManagement service call here

    def getNoOfBarters(self) -> int:
        return len(self._barterIDs)

    def hasBarters(self) -> bool:
        if self.getNoOfBarters() > 0:
            return True
        else:
            return False

    def synchronizeDB(self) -> None:
        from StoreManagement.Boundaries.DAOs.ProductDAO import ProductDAO
        dao = ProductDAO()
        dao.update(self)

    # getters and setters
    def getID(self) -> int:
        return self._productID

    def setID(self, newID: int) -> None:
        self._productID = newID

    def getName(self) -> str:
        return self._name

    def setName(self, name: str) -> None:
        self._name = name

    def setDescription(self, description: str) -> None:
        self._description = description

    def getDescription(self) -> str:
        return self._description

    def getLocation(self) -> str:
        return self._currentLocation

    def setLocation(self, location: str) -> None:
        self._currentLocation = location

    def getDate(self) -> datetime.datetime:
        return self._creationDate

    def setDate(self, date: datetime.datetime) -> None:
        self._creationDate = date

    def getCategory(self) -> CategoryProxy:
        return self._category

    def setCategory(self, category: CategoryProxy) -> None:
        self._category = category

    def getStore(self) -> StoreProxy:
        return self._store

    def setStore(self, store: StoreProxy) -> None:
        self._store = store

    def getImageIDs(self) -> int:
        return self._imageIDs

    def setImageIDs(self, imageIDs: [int]) -> None:
        self._imageIDs = imageIDs

    def getBarterIDs(self) -> [int]:
        return self._barterIDs

    def setBarterIDs(self, barterIDs: []) -> None:
        self._barterIDs = barterIDs





