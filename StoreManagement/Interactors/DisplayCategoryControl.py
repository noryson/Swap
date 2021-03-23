from StoreManagement.Entities.CategoryProxy import CategoryProxy
from Exceptions.CategoryExceptions import *


class DisplayCategoryControl:
    """" invariants:
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

    def execute(self):
        return self._category