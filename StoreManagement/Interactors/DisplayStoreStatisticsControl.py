from StoreManagement.Entities.StoreProxy import StoreProxy
from Exceptions.StoreExceptions import *


class DisplayStoreStatisticsControl:
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
    """

    def execute(self) -> []:
        statistics = self._store.calculateStatistics()
        return statistics
