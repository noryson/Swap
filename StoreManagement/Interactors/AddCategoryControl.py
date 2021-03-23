from StoreManagement.Boundaries.DAOs.CategoryDAO import CategoryDAO

class AddCategoryControl:
    """ invariants:
    """

    _name: str = None

    def __init__(self, name: str) -> None:
        self._name = name

    """ execute()
        @pre allCategory.name !contain name
    """
    def execute(self) -> None:
        from StoreManagement.Interactors.DisplayCategoriesControl import DisplayCategoriesControl
        control = DisplayCategoriesControl()
        myCategories = control.execute()

        for cat in myCategories:
            if cat.name == self._name:
                raise RuntimeError('Category name already in use: ' + self._name )

        dao = CategoryDAO()
        dao.create(self._name)
