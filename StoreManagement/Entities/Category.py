class Category:
    _categoryID: int = None
    _name: str = None

    def changeName(self, name) -> None:
        self.setName(name)
        self.synchronizeDB()

    # helpers
    def synchronizeDB(self) -> None:
        from StoreManagement.Boundaries.DAOs.CategoryDAO import CategoryDAO
        dao = CategoryDAO()
        dao.update(self)

    # getters and setters
    def getID(self) -> int:
        return self._categoryID

    def setID(self, newID: int) -> None:
        self._categoryID = newID

    def getName(self) -> str:
        return self._name

    def setName(self, name) -> None:
        self._name = name
