import datetime
import BarterManagement.Boundaries.BarterDAO as BarterDAOModule
from StoreManagement.Boundaries.Services import StoreService
from Exceptions.BarterExceptions import *


class HostBarterControl:
    """ invariants:
        @inv getMaxNoOfBarters() > 0
        @inv getMaxNoOfOffers() > 0
        @inv getMaxNoOfProofs() > 0
        @inv getProduct() != None
        @inv getEndDate() != None
        @inv store.getProducts() contains product
        @inv getrequestedItem() != None
    """

    _maxNoOfBarters: int = None
    _productID: int = None
    _endDate: datetime.datetime = None
    _requestedItem: str = None

    """ __init__() takes the DTO and initializes all class attributes
    """
    def __init__(self, productID: int, endDate: datetime.datetime, requestedItem: str) -> None:
        self.setProductID(productID)
        self._endDate: datetime = endDate
        self.setRequest(requestedItem)

    """ execute() takes the provided data and creates the barter
        @pre isStoreLimitExceeded() = False 
        @pre getEndDate() > 1 week
        @pre product.getBarters().is['running','transferring', 'concluded'] = False
        @post product.getBarters().isRunning() = True
        @post store.getNoOfBarters() = self.store.getNoOfBarters() + 1
        @post store.getBarters() contains getBarter()
    """
    def execute(self) -> None:
        service: StoreService = StoreService()

        if not service.canProductHostBarter(self.getProductID()):
            raise RuntimeError(self.getProductID())

        try:
            if (datetime.datetime.now() + datetime.timedelta(weeks=1)) > self._endDate:
                raise BarterHasInvalidDateException
        except BarterHasInvalidDateException:
            raise RuntimeError("Barter has invalid duration")

        # dao: BarterDAOModule = BarterDAOModule.BarterDAO()
        from BarterManagement.Boundaries.BarterDAO import BarterDAO
        dao: BarterDAO = BarterDAO()
        dao.create(self._productID, self._requestedItem, self._endDate)

    """ notifySubscribers() sends a notification to all buyers subscribed to the store
        @pre store.getSubscribers() != None
    """
    def notifySubscribers(self) -> None:
        # try:
        #     subscribers = self._product.getStore().getSubscribers()
        # except StoreHasNoSubscribersException as exc:
        #     print(exc.args)
        # else:
        #     for subscriber in subscribers:
        #         if not subscriber.isDeactivated():
        #             notify(self._product.getStore().getOwner().getID(), subscriber,
        #                    self._product.getStore().getOwner().getFullName() + 'hosted a new barter')
        pass

    # getters and setters
    def getProductID(self) -> int:
        return self._productID

    def setProductID(self, newProductID: int) -> None:
        self._productID = newProductID

    def getEndDate(self) -> datetime:
        return self._endDate

    def setEndDate(self, newDate: datetime) -> None:
        self._endDate = newDate

    def getRequest(self) -> str:
        return self._requestedItem

    def setRequest(self, newRequest: str):
        self._requestedItem = newRequest
