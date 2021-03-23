from StoreManagement.Entities.StoreProxy import StoreProxy
from Exceptions.StoreExceptions import *


class ActivateStoreControl:
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
        @pre store.isActive() = False
        @post store.isActive() = True
    """
    def execute(self) -> None:
        try:
            self._store.activate()
        except StoreIsActiveException:
            raise RuntimeError('store is active' + str(self._store.getID()))
        except PermissionError:
            raise RuntimeError('Access denied' + str(self._store.getID()))
