from BarterManagement.Boundaries.DTO import BarterDTO
from Exceptions.BarterExceptions import BarterNotFoundException
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BarterManagement.Entities.Barter import Barter
from BarterManagement.Entities.BarterProxy import BarterProxy


class GetBarterControl:
    """ invariants:
        @inv barter != None
    """

    _barter: 'BarterProxy' = None

    def __init__(self, barterID: int) -> None:
        try:
            barterProxy: BarterProxy = BarterProxy()
            barterProxy.setRealBarterID(barterID)
            barterProxy.proxyCheck()
            self.setBarter(barterProxy)
        except BarterNotFoundException:
            raise RuntimeError("Barter not found.")

    def execute(self):  # Return type should be dto or barterProxy
        barter = self.getBarter()
        # dto = BarterDTO()
        # dto.setID(barter.getID())
        # dto.setRequest(barter.getRequest())
        # dto.setEndDate(barter.getEndDate())
        # dto.setStatus(barter.getStatus())
        # dto.setAdminStatus(barter.getAdminStatus())
        # dto.setOfferIDs(barter.getOffersID())
        # dto.setProductID(barter.getProductID)
        # return dto
        return barter

    def getBarter(self) -> BarterProxy:
        return self._barter

    def setBarter(self, newBarter: BarterProxy) -> None:
        self._barter = newBarter