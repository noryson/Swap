from StoreManagement.Entities.CategoryProxy import CategoryProxy
from StoreManagement.Boundaries.DAOs.CategoryDAO import CategoryDAO
from Exceptions.CategoryExceptions import *


class UpdateCategoryNameControl:
    """" invariants:
    """

    _category: CategoryProxy = None
    _name: str = None

    def __init__(self, categoryID: int, name: str) -> None:
        try:
            categoryProxy: CategoryProxy = CategoryProxy()
            categoryProxy.setRealCategoryID(categoryID)
            categoryProxy.proxyCheck()
        except CategoryNotFoundException:
            raise RuntimeError("Category does not exist " + str(categoryID))

        self._category = categoryProxy
        self._name = name

    """ execute()
        @pre allCategories.getName() == name
    """
    def execute(self) -> None:
        from StoreManagement.Interactors.DisplayCategoriesControl import DisplayCategoriesControl
        control = DisplayCategoriesControl()
        categories = control.execute()
        for cat in categories:
            if cat.name == self._name:
                raise CategoryNameExistException(self._name)

        self._category.changeName(self._name)