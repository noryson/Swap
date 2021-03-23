from BarterManagement.Entities.Barter import Barter
from BarterManagement.Boundaries.BarterDAO import BarterDAO
from BarterManagement.Entities.BarterProxy import BarterProxy
from BarterManagement.Entities.BarterAccess import BarterAccess
from BarterManagement.Boundaries.OfferDAO import OfferDAO
from Exceptions.BarterExceptions import *

class PlaceOfferControl:
    """ invariants:
        @inv no field is None
        @inv buyer.getNoOfOffers() > maxNoOfOffer
        @inv buyer != barter.seller
        @inv product.barter = barter
        @inv barter.getOffers().owners !include buyer
    """

    _barter: BarterProxy = None
    _offeredItem: str = None
    _maxNoOfOffers: int = None
    _currentUserID: int = None

    def __init__(self, barterID: int, offeredItem: str) -> None:
        try:
            barterProxy: BarterProxy = BarterProxy()
            barterProxy.setRealBarterID(barterID)
            barterProxy.proxyCheck()
            self.setBarter(barterProxy)

            self.setOfferedItem(offeredItem)
        except BarterNotFoundException:
            raise RuntimeError()

    """ execute() 
        @pre barter.isConcluded() = False
        @pre barter.isTransferring() = False
        @pre barter.isTerminated() = False
        @pre offerDTO.owner != product.getOwner()
        @pre offerDTO.owner !contains getOffers().owners
        @post getOffers() contain offerDTO
        @post getNoOfOffers() = @self.getNoOfOffers + 1
    """
    def execute(self) -> None:
        try:
            barter = self.getBarter()
            if barter.isDeactivated():
                raise BarterDeactivatedException(barter.getID())
            if barter.isConcluded():
                raise BarterConcludedException(barter.getID())
            if barter.isTerminated():
                raise BarterTerminatedException(barter.getID())
            if barter.isTransferring():
                raise BarterTransferringException(barter.getID())
        except BarterDeactivatedException:
            raise RuntimeError()
        except BarterConcludedException:
            raise RuntimeError()
        except BarterTerminatedException:
            raise RuntimeError()
        except BarterTransferringException:
            raise RuntimeError('Barter is in transfer state')

        try:
            for offer in self._barter.getOffers():
                if offer.getBuyer.getID() == self._currentUserID:
                    raise BarterHasAnOfferFromBuyerException(self._barter.getID())
        except BarterHasAnOfferFromBuyerException:
            raise RuntimeError()

        try:
            barter: BarterProxy = self.getBarter()
            access: BarterAccess = BarterAccess(barter._realBarter)
            if not access.isAccessible('placeOffer'):
                raise PermissionError(access)

            offerDao = OfferDAO()
            newID = offerDao.create(self.getOfferedItem(), barter.getID(), self._currentUserID)

        except PermissionError:
            raise RuntimeError()

    def notifySeller(self) -> None:
        seller = self.getBarter().getProduct().getStore().getOwnerID()
        # notify(seller, 'You have a new offer')

    # getters and setters
    def getOfferedItem(self) -> str:
        return self._offeredItem

    def setOfferedItem(self, newItem: str) -> None:
        self._offeredItem = newItem

    def getBarter(self) -> BarterProxy:
        return self._barter

    def setBarter(self, newBarter: BarterProxy) -> None:
        self._barter = newBarter
