from BarterManagement.Boundaries.OfferDAO import OfferDAO
from BarterManagement.Entities.OfferProxy import OfferProxy
from Exceptions.BarterExceptions import *
from Exceptions.OfferExceptions import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BarterManagement.Entities.Offer import Offer


class DeclineOfferControl:
    """ invariants:
        @inv no None attributes
    """

    _offer: OfferProxy = None

    def __init__(self, offerID: int) -> None:
        try:
            offerProxy: OfferProxy = OfferProxy()
            offerProxy.setRealOfferID(offerID)
            offerProxy.proxyCheck()
            self.setOffer(offerProxy)
        except OfferNotFoundException:
            raise RuntimeError()

    """ execute()
        @pre offer.isAccepted() = True
        @pre offer.barter.is[concluded, terminated, transferring] = False
        @pre offer.hasProof() = False
        @post offer.isAccepted() = False
        @post offer.isTransferring() = True
    """
    def execute(self):
        try:
            self.getOffer().decline()
        except BarterDeactivatedException:
            raise RuntimeError()
        except BarterConcludedException:
            raise RuntimeError()
        except BarterTerminatedException:
            raise RuntimeError()
        except OfferNotAcceptedException:
            raise RuntimeError()
        except OfferHasProofException:
            raise RuntimeError()
        except PermissionError:
            raise RuntimeError()

    def notifyBuyer(self):
        # notify(self.getOffer().getBuyerID(), 'You offer has been rejected')
        pass

    def getOffer(self) -> OfferProxy:
        return self._offer

    def setOffer(self, newOffer: OfferProxy) -> None:
        self._offer = newOffer