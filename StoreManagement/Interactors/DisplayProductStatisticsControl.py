from StoreManagement.Entities.ProductProxy import ProductProxy
from Exceptions.ProductExceptions import *


class DisplayProductControl:
    """ invariants:
    """

    _product: ProductProxy = None

    def __init__(self, productID: int) -> None:
        try:
            productProxy = ProductProxy()
            productProxy.setRealProductID(productID)
            productProxy.proxyCheck()
        except ProductNotFoundException:
            raise RuntimeError('Product not found' + str(productID))

        self._product = productProxy

    def execute(self) -> []:
        return self._product.calculateStatistics()
