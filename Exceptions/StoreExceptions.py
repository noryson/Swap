class StoreException(BaseException):
    pass


class StoreLimitExceededException(StoreException):
    pass


class StoreHasNoSubscribersException(StoreException):
    pass


class StoreIsDeactivatedException(StoreException):
    pass


class StoreIsActiveException(StoreException):
    pass


class StoreSubscriberNonExistentException(StoreException):
    pass


class StoreSubscriberExistException(StoreException):
    pass


class StoreCreationFailedException(StoreException):
    pass


class StoreNotFoundException(StoreException):
    pass


class StoreUpdateFailureException(StoreException):
    pass


class StoreDeleteFailureException(StoreException):
    pass