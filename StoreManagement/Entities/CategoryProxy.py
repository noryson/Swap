import datetime
from StoreManagement.Entities.CategoryAccess import CategoryAccess
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from StoreManagement.Entities.Category import Category


class CategoryProxy:
    """ invariants:
    """

    _realCategoryID: int = None
    _realCategory: Category = None
    _access: CategoryAccess = None

    def proxyCheck(self) -> None:
        if self._realCategory is None:
            from StoreManagement.Boundaries.DAOs.CategoryDAO import CategoryDAO
            dao = CategoryDAO()
            self._realCategory = dao.get(self._realCategoryID)
            self._access = CategoryAccess(self._realCategory)

    def getRealCategoryID(self) -> int:
        return self._realCategoryID

    def setRealCategoryID(self, newID: int) -> None:
        self._realCategoryID = newID

    # main Category Calls
    def changeName(self, name) -> None:
        self.proxyCheck()
        self._realCategory.changeName(name)

    # getters and setters
    def getID(self) -> int:
        self.proxyCheck()
        return self._realCategory.getID()

    def setID(self, newID: int) -> None:
        self.proxyCheck()
        self._realCategory.setID(newID)

    def getName(self) -> str:
        self.proxyCheck()
        return self._realCategory.getName()

    def setName(self, name) -> None:
        self.proxyCheck()
        self._realCategory.setName(name)

