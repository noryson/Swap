class BarterException(BaseException):
    pass


class BarterNotFoundException(BarterException):
    pass


class BarterAlreadyExistException(BarterException):
    pass


class BarterConcludedException(BarterException):
    pass


class BarterTerminatedException(BarterException):
    pass


class BarterDeactivatedException(BarterException):
    pass


class BarterTransferringException(BarterException):
    pass


class BarterNotTransferringException(BarterException):
    pass


class BarterHasNoOfferException(BarterException):
    pass


class MaxNoOfBarterExceededException(BarterException):
    pass


class BarterAccessDenied(BarterException):
    pass


class BarterHasNoProductException(BarterException):
    pass


class BarterHasAcceptanceException(BarterException):
    pass


class BarterHasNoAcceptanceException(BarterException):
    pass


class BarterHasProofException(BarterException):
    pass


class BarterHasAnOfferFromBuyerException(BarterException):
    pass


class BarterHasInvalidDateException(BarterException):
    pass


class BarterUpdateFailException(BarterException):
    pass


class BarterDeleteFailException(BarterException):
    pass


class BarterCreationFailException(BarterException):
    pass