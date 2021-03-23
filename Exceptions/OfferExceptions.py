class OfferException(BaseException):
    pass


class OfferHasProofException(OfferException):
    pass


class OfferHasNoProofException(OfferException):
    pass


class OfferAlreadyExistException(OfferException):
    pass


class OfferNotInBarterException(OfferException):
    pass


class OfferIsAcceptedException(OfferException):
    pass


class OfferNotAcceptedException(OfferException):
    pass


class OfferDoesNotExistException(OfferException):
    pass


class OfferNotFoundException(OfferException):
    pass


class OfferCreationFailedException(OfferException):
    pass


class OfferUpdateFailedException(OfferException):
    pass


class OfferDeleteFailedException(OfferException):
    pass

