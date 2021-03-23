from StoreManagement.Entities.StoreProxy import StoreProxy
from Exceptions.StoreExceptions import *


class DeactivateStoreControl:
    """ invariants:
    """

    _store: StoreProxy = None

    def __init__(self, storeID: int) -> None:
        try:
            storeProxy: StoreProxy = StoreProxy()
            storeProxy.setRealStoreID(storeID)
            storeProxy.proxyCheck()
        except StoreNotFoundException:
            raise RuntimeError("store not found" + str(storeID))

        self._store = storeProxy

    """ execute()
        @pre store.isActive() = True
        @post store.isActive() = False
    """
    def execute(self) -> None:
        try:
            self._store.deactivate()
        except StoreIsDeactivatedException:
            raise RuntimeError('store is inactive' + str(self._store.getID()))
        except PermissionError:
            raise RuntimeError('Access denied' + str(self._store.getID()))
