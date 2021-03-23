import datetime
from StoreManagement.Entities.ProductAccess import ProductAccess
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from StoreManagement.Entities.Product import Product
    from StoreManagement.Entities.StoreProxy import StoreProxy
    from StoreManagement.Entities.CategoryProxy import CategoryProxy


class ProductProxy:
    """ invariants:
    """

    _realProductID: int = None
    _realProduct: Product = None
    _access: ProductAccess = None

    def proxyCheck(self) -> None:
        if self._realProduct is None:
            from StoreManagement.Boundaries.DAOs.ProductDAO import ProductDAO
            dao = ProductDAO()
            self._realProduct = dao.get(self._realProductID)
            self._access = ProductAccess(self._realProduct)

    def getRealProductID(self) -> int:
        return self._realProductID

    def setRealProductID(self, newID: int) -> None:
        self._realProductID = newID

    # Main Product Calls
    def changeLocation(self, location: str) -> None:
        self.proxyCheck()
        if not self._access.isAccessible("changeLocation"):
            raise PermissionError(self._access)
        else:
            self._realProduct.setLocation(location)

    def calculateStatistics(self) -> {}:
        self.proxyCheck()
        return self._realProduct.calculateStatistics()

    # helpers and checkers
    def isSwapped(self) -> bool:
        self.proxyCheck()
        return self._realProduct.isSwapped()

    def getNoOfBarters(self) -> int:
        self.proxyCheck()
        return self._realProduct.getNoOfBarters()

    def hasBarters(self) -> bool:
        self.proxyCheck()
        return self._realProduct.hasBarters()

    # getters and setters
    def getID(self) -> int:
        self.proxyCheck()
        return self._realProduct.getID()

    def setID(self, newID: int) -> None:
        self.proxyCheck()
        self._realProduct.setID(newID)

    def getName(self) -> str:
        self.proxyCheck()
        return self._realProduct.getName()

    def setName(self, name: str) -> None:
        self.proxyCheck()
        self._realProduct.setName(name)

    def setDescription(self, description: str) -> None:
        self.proxyCheck()
        self._realProduct.setDescription(description)

    def getDescription(self) -> str:
        self.proxyCheck()
        return self._realProduct.getDescription()

    def getLocation(self) -> str:
        self.proxyCheck()
        return self._realProduct.getLocation()

    def setLocation(self, location: str) -> None:
        self.proxyCheck()
        self._realProduct.setLocation(location)

    def getDate(self) -> datetime.datetime:
        self.proxyCheck()
        return self._realProduct.getDate()

    def setDate(self, date: datetime.datetime) -> None:
        self.proxyCheck()
        self._realProduct.setDate(date)

    def getCategory(self) -> CategoryProxy:
        self.proxyCheck()
        return self._realProduct.getCategory()

    def setCategory(self, category: CategoryProxy) -> None:
        self.proxyCheck()
        self._realProduct.setCategory(category)

    def getStore(self) -> StoreProxy:
        self.proxyCheck()
        return self._realProduct.getStore()

    def setStore(self, store: StoreProxy) -> None:
        self.proxyCheck()
        self._realProduct.setStore(store)

    def getImageIDs(self) -> int:
        self.proxyCheck()
        return self._realProduct.getImageIDs()

    def setImageIDs(self, imageIDs: [int]) -> None:
        self.proxyCheck()
        self._realProduct.setImageIDs(imageIDs)

    def getBarterIDs(self) -> [int]:
        self.proxyCheck()
        return self._realProduct.getBarterIDs()

    def setBarterIDs(self, barterIDs: []) -> None:
        self.proxyCheck()
        self._realProduct.setBarterIDs(barterIDs)
