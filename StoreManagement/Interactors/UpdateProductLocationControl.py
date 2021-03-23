from StoreManagement.Entities.ProductProxy import ProductProxy
from Exceptions.ProductExceptions import *
from Exceptions.StoreExceptions import *


class UpdateProductLocationControl:
    """ invariants:
    """

    _product: ProductProxy = None
    _location: str = None

    def __init__(self, productID: int, location: str) -> None:
        try:
            productProxy = ProductProxy()
            productProxy.setRealProductID(productID)
            productProxy.proxyCheck()
        except ProductNotFoundException:
            raise RuntimeError('Product not found' + str(productID))

        self._product = productProxy
        self._location = location

    def execute(self) -> None:
        try:
            self._product.changeLocation(self._location)
        except ProductIsSwappedException:
            raise RuntimeError('Product is swapped')
        except StoreIsDeactivatedException:
            raise RuntimeError("Store is inactive")
