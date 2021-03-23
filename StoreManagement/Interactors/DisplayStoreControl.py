from StoreManagement.Entities.StoreProxy import StoreProxy
from Exceptions.StoreExceptions import *


class DisplayStoreControl:
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
    def execute(self):
        store = self._store
        return store
