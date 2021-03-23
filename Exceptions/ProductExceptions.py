class ProductException(BaseException):
    pass


class ProductNotFoundException(ProductException):
    pass


class ProductIsBarteringException(ProductException):
    pass


class ProductIsSwappedException(ProductException):
    pass


class ProductCreationFailedException(ProductException):
    pass


class ProductUpdateFailureException(ProductException):
    pass


class ProductDeleteFailureException(ProductException):
    pass