from UserManagement.Boundaries.CurrentUserService import CurrentUserService
from UserManagement.Entities.UserProxy import UserProxy
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from StoreManagement.Entities.Product import Product


class ProductAccess:
    _product: Product = None
    _currentUserID: int = None
    _userService: CurrentUserService = None

    def __init__(self, product: Product):
        self._product = product
        self._userService = CurrentUserService()
        self._currentUserID = self._userService.getCurrentUserID()

    def isAccessible(self, operation) -> bool:
        ownerID: int = self._product.getStore().getOwnerID()

        currentUserID: int = self._currentUserID
        currentUser = UserProxy()
        currentUser.setRealUserID(currentUserID)

        if operation == "changeLocation":
            if currentUserID == ownerID:
                return True
            if currentUser.isStaff() and currentUser.hasProductPrivilege('write'):
                return True
            else:
                return False

        if operation == 'delete':
            if currentUserID == ownerID:
                return True
            if currentUser.isStaff() and currentUser.hasProductPrivilege('write'):
                return True
            else:
                return False
