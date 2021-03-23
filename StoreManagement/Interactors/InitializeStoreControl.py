class InitializeStoreControl:
    """ invariants:
    """

    _ownerID: int = None
    _maxNoOfProducts: int = None

    def __init__(self, ownerID: int, maxNoOfProduct: int) -> None:
        self._ownerID = ownerID
        self._maxNoOfProducts = maxNoOfProduct

    """execute()
        @pre owner.hasStore == False
    """
    def execute(self) -> None:
        service = UserService()
        if not service.hasStore(self._ownerID):
            raise RuntimeError("User has a store" + str(self._ownerID))

        from StoreManagement.Boundaries.DAOs.StoreDAO import StoreDAO
        dao = StoreDAO()
        dao.create(self._ownerID, self._maxNoOfProducts)

