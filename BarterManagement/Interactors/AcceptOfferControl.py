from BarterManagement.Boundaries.OfferDAO import OfferDAO
from BarterManagement.Entities.OfferProxy import OfferProxy
from Exceptions.BarterExceptions import *
from Exceptions.OfferExceptions import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BarterManagement.Entities.Offer import Offer


class AcceptOfferControl:
    """ invariants:
        @inv offer.getProduct().getBarter != None
        @inv getBuyer() != None
    """

    _offer: OfferProxy = None

    def __init__(self, offerID: int) -> None:
        try:
            offerProxy: OfferProxy = OfferProxy()
            offerProxy.setRealOfferID(offerID)
            offerProxy.proxyCheck()
            self.setOffer(offerProxy)
        except OfferNotFoundException:
            raise RuntimeError(offerID)

    """ execute()
        @pre offer.barter.isTransferring() = False
        @pre offerDTO.owner !contains getOffers().owners
        @pre getAcceptedOffer() = None
        @pre barter.isConcluded() = False
        @pre barter.isTransferring = False
        @pre barter.isAccepted() = False
        @post barter.isTransferring = True
        @post isAccepted = True
        @post getAcceptedOffer() = offer
        @post offer.barter.isTransferring() = True
    """
    def execute(self) -> None:
        try:
            self.getOffer().accept()
        except BarterDeactivatedException:
            raise RuntimeError()
        except BarterConcludedException:
            raise RuntimeError()
        except BarterTerminatedException:
            raise RuntimeError()
        except BarterTransferringException:
            raise RuntimeError("barter has accepted an offer previously")
        except OfferIsAcceptedException:
            raise RuntimeError()
        except PermissionError:
            raise RuntimeError()

    def notifyBuyer(self) -> None:
        # notify(self.getOffer().getBuyerID(), 'You offer has been accepted')
        pass

    # getters and setters
    def getOffer(self) -> OfferProxy:
        return self._offer

    def setOffer(self, newOffer: OfferProxy) -> None:
        self._offer = newOffer