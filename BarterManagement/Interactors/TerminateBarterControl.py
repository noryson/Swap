from BarterManagement.Entities.BarterProxy import BarterProxy
from BarterManagement.Boundaries.DTO import BarterDTO
from Exceptions.BarterExceptions import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BarterManagement.Entities.Barter import Barter


class TerminateBarterControl:
    """ invariants:
        @inv barter != None
    """
    _barter: BarterProxy = None

    def __init__(self, barterID: int) -> None:
        try:
            barterProxy: BarterProxy = BarterProxy()
            barterProxy.setRealBarterID(barterID)
            barterProxy.proxyCheck()
            self.setBarter(barterProxy)
        except BarterNotFoundException:
            raise RuntimeError("Barter not found")

    """ execute()
        @pre barter.hasProof() = False
        @post store.getNoOfBarters() = self.store.getNoOfBarters() - 1
    """
    def execute(self):
        try:
            self.getBarter().terminate()
        except BarterTransferringException:
            raise RuntimeError('Barter is in transferring state')
        except BarterDeactivatedException or BarterConcludedException or BarterTerminatedException:
            raise RuntimeError("Invalid Operation")
        except PermissionError:
            raise RuntimeError("Access denied")

    def notifyInterestGroup(self):
        # interestGroup: [] = None
        # for offer in self.getBarter().getOffers():
        #     interestGroup.append(offer.getBuyerID())
        #
        # for buyer in interestGroup:
        #     # notify()
        #     pass
        pass
            
    # getters and setters
    def getBarter(self) -> BarterProxy:
        return self._barter

    def setBarter(self, newBarter: BarterProxy) -> None:
        self._barter = newBarter