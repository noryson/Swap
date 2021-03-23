from StoreManagement.Entities.StoreProxy import StoreProxy
from UserManagement.Boundaries.CurrentUserService import CurrentUserService
from Exceptions.StoreExceptions import *


class SubscribeToStoreControl:
    """ invariants:
    """

    _store: StoreProxy = None
    _subscriberID: int = None

    def __init__(self, storeID: int) -> None:
        try:
            storeProxy: StoreProxy = StoreProxy()
            storeProxy.setRealStoreID(storeID)
            storeProxy.proxyCheck()
        except StoreNotFoundException:
            raise RuntimeError("store not found" + str(storeID))

        userService = CurrentUserService()
        currentUserID = userService.getCurrentUserID()

        self._store = storeProxy
        self._subscriberID = currentUserID

    """ execute()
        @pre store.isActive() = False
        @post store.isActive() = True
    """
    def execute(self) -> None:
        try:
            self._store.subscribe(self._subscriberID)
        except StoreIsDeactivatedException:
            raise RuntimeError('store is inactive' + str(self._store.getID()))
        except StoreSubscriberExistException:
            raise RuntimeError('this user is already subscribed to this store')
        except PermissionError:
            raise RuntimeError('Access denied' + str(self._store.getID()))
