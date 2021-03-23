class Subscription:
    _storeID: int = None
    _userIDs: [int] = None

    def subscribe(self, userID: int) -> None:
        pass

    def unsubscribe(self, userID: int) -> None:
        pass

    # helpers and checkers
    def isSubscribed(self, userID: int) -> bool:
        pass

    # getters and setters
    def getStoreID(self) -> int:
        return self._storeID

    def setStoreID(self, storeID) -> None:
        pass