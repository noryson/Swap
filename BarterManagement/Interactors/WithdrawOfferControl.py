from BarterManagement.Boundaries.OfferDAO import OfferDAO
from BarterManagement.Entities.OfferProxy import OfferProxy
from BarterManagement.Entities.OfferAccess import OfferAccess
from BarterManagement.Entities.BarterProxy import BarterProxy
from Exceptions.BarterExceptions import *
from Exceptions.OfferExceptions import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BarterManagement.Entities.Offer import Offer


class WithdrawOfferControl:
    """ invariants:
        @inv no None attributes
    """

    _offer: OfferProxy = None

    def __init__(self, offerID: int):
        try:
            offerProxy: OfferProxy = OfferProxy()
            offerProxy.setRealOfferID(offerID)
            offerProxy.proxyCheck()
            self.setOffer(offerProxy)
        except OfferNotFoundException:
            raise RuntimeError()

    """ execute()
        @pre barter.isDeactivated(), isConcluded(), isTerminated() = False
        @pre offers.contains offer
        @pre offer.isAccepted() = False
        @post offers.!contain offer
    """
    def execute(self):
        barter: BarterProxy = self.getOffer().getBarter()
        try:
            if barter.isDeactivated():
                raise BarterDeactivatedException(barter.getID())
            if barter.isConcluded():
                raise BarterConcludedException(barter.getID())
            if barter.isTerminated():
                raise BarterTerminatedException(barter.getID())
            if barter.isTransferring():
                raise BarterTransferringException(barter.getID())
        except BarterDeactivatedException:
            raise RuntimeError('Barter deactivate')
        except BarterConcludedException:
            raise RuntimeError('Barter concluded')
        except BarterTransferringException:
            raise RuntimeError('Barter transferring')

        try:
            offer: OfferProxy = self.getOffer()
            access: OfferAccess = OfferAccess(offer._realOffer)
            if not access.isAccessible('withdrawOffer'):
                raise PermissionError(access)
        except PermissionError:
            raise RuntimeError('Access denied')

        try:
            for myOffer in barter.getOffers():
                if self.getOffer().getID() == myOffer.getID():
                    if not self.getOffer().isAccepted():
                        offerDao = OfferDAO()
                        offerDao.delete(self.getOffer().getID())
                        return
                    else:
                        raise OfferIsAcceptedException(self.getOffer().getID())
            raise OfferNotInBarterException(self.getOffer().getID())
        except OfferIsAcceptedException:
            raise RuntimeError('Offer is accepted')
        except OfferNotInBarterException:
            raise RuntimeError('offer not in barter')

    def notifySeller(self):
        seller = self.getOffer().getBarter().getProduct().getStore().getOwnerID()
        # notify(seller, 'You have a new offer')

    # getters and setters
    def getOffer(self) -> OfferProxy:
        return self._offer

    def setOffer(self, newOffer: OfferProxy) -> None:
        self._offer = newOffer