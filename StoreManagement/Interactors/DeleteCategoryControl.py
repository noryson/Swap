from StoreManagement.Entities.CategoryProxy import CategoryProxy
from StoreManagement.Entities.CategoryAccess import CategoryAccess
from StoreManagement.Boundaries.DAOs.CategoryDAO import CategoryDAO
from Exceptions.CategoryExceptions import *


class DeleteCategoryControl:
    """ invariants:
        @ inv
    """

    _category: CategoryProxy = None

    def __init__(self, categoryID: int) -> None:
        try:
            categoryProxy: CategoryProxy = CategoryProxy()
            categoryProxy.setRealCategoryID(categoryID)
            categoryProxy.proxyCheck()
        except CategoryNotFoundException:
            raise RuntimeError("Category does not exist " + str(categoryID))

        self._category = categoryProxy

    def execute(self) -> None:
        access = CategoryAccess(self._category._realCategory)
        if not access.isAccessible('delete'):
            raise PermissionError("You cant delete this item" + str(self._product.getID()))

        dao = CategoryDAO()
        dao.delete(self._category.getID())