from StoreManagement.Entities.CategoryProxy import CategoryProxy
from StoreManagement.Boundaries.DAOs.CategoryDAO import CategoryDAO
from Exceptions.CategoryExceptions import *


class DisplayCategoriesControl:
    """" invariants:
    """

    _categories: [CategoryProxy] = None

    def __init__(self) -> None:
        try:
            dao = CategoryDAO()
            categories = dao.getAll()
            for cat in categories:
                categoryProxy: CategoryProxy = CategoryProxy()
                categoryProxy.setRealCategoryID(cat.getID())
                self._category.append(categoryProxy)
        except CategoryNotFoundException:
            raise RuntimeError("No category created yet")

    def execute(self) -> []:
        return self._categories