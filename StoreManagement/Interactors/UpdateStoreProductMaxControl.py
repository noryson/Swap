from StoreManagement.Entities.StoreProxy import StoreProxy
from Exceptions.StoreExceptions import *


class UpdateStoreProductMaxControl:
    """ invariants:
        """

    _store: StoreProxy = None
    _maxNoOfProducts: int = None

    def __init__(self, storeID: int, maxNoOfProducts: int) -> None:
        try:
            storeProxy: StoreProxy = StoreProxy()
            storeProxy.setRealStoreID(storeID)
            storeProxy.proxyCheck()
        except StoreNotFoundException:
            raise RuntimeError("store not found" + str(storeID))

        self._store = storeProxy
        self._maxNoOfProducts = maxNoOfProducts

    """ execute()
        @pre store.isActive() = True
    """

    def execute(self) -> None:
        try:
            self._store.changeMaxNoOfProduct(self._maxNoOfProducts)
        except ValueError:
            raise RuntimeError('Invalid max no')
        except StoreIsDeactivatedException:
            raise RuntimeError('store is inactive' + str(self._store.getID()))
        except PermissionError:
            raise RuntimeError('Access denied' + str(self._store.getID()))
