from StoreManagement.Entities.ProductProxy import ProductProxy
from StoreManagement.Entities.ProductAccess import ProductAccess
from StoreManagement.Boundaries.DAOs.ProductDAO import ProductDAO
from Exceptions.ProductExceptions import *


class DeleteProductControl:
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

    def execute(self) -> None:
        access = ProductAccess(self._product._realProduct)
        if not access.isAccessible('delete'):
            raise PermissionError("You cant delete this item" + str(self._product.getID()))

        dao = ProductDAO()
        dao.delete(self._product.getID())
