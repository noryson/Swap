import datetime
from BarterManagement.Entities.BarterProxy import BarterProxy as Barter
from BarterManagement.Boundaries.DTO import BarterDTO
import BarterManagement.Boundaries.BarterDAO as BarterDAO
from BarterManagement.Entities.ProductProxy import ProductProxy as Product
from BarterManagement.Entities.StoreProxy import StoreProxy as Store
from Exceptions.BarterExceptions import *


class FindBarterControl:
    """ invariants:
        @inv no None field
    """

    def __init__(self, query: str, requestedItem: str = 'all', category: str = 'all', limit: int = 30, sort: str = 'name',
                 order: str = 'desc', status: str = 'running', adminStatus: str = 'active', page: int = 1) -> None:
        self._query = query
        self._category = category
        self._requestedItem = requestedItem
        self._page = page

        if limit > 100:
            self._limit = 100
        else:
            self._limit = limit

        if sort != 'name' or sort != 'date':
            self._sort = 'name'
        else:
            self._sort = sort

        if order != 'asc' or self._order != 'desc':
            self._order = 'desc'
        else:
            self._order = order

        if adminStatus != 'active' or adminStatus != 'deactivated':
            self._adminStatus = 'active'
        else:
            self._adminStatus = adminStatus

        if status != 'running' or status != 'terminated' or status != 'concluded' or status != 'transferring':
            self._status = 'running'
        else:
            self._status = status

    def execute(self) -> []:
        try:
            dao = BarterDAO.BarterDAO()
            result: [] = dao.find(self._query, requestedItem=self._requestedItem, category=self._category,
                                  limit=self._limit, page=self._page, status=self._status, adminStatus=self._adminStatus,
                                  sort=self._sort, order=self._order)
        except BarterNotFoundException as exc:
            raise RuntimeError("No Barter found.")
        else:
            # resultDto: [] = []
            # dto = BarterDTO
            # for barter in result:
            #     dto.setBarterID(barter.getID())
            #     dto.setRequest(barter.getRequest())
            #     dto.setEndDate(barter.getEndDate())
            #     dto.setStatus(barter.getStatus())
            #     dto.setAdminStatus(barter.getAdminStatus())
            #     dto.setOfferIDs(barter.getOffersID())
            #     dto.setProductID(barter.getProductID)
            #     resultDto.append(dto)
            # return resultDto
            return result

    # getters and setters
    def getStartDate(self) -> datetime:
        return self._startDate

    def setStartDate(self, newDate) -> None:
        self._startDate = newDate

    def getEndDate(self) -> datetime:
        return self._endDate

    def setEndDate(self, newDate) -> None:
        self._endDate = newDate

    def getStatus(self) -> str:
        return self._status

    def setStatus(self, newStatus) -> None:
        self._status = newStatus

    def getProductID(self) -> int:
        return self._productID

    def setProductID(self, newID) -> None:
        self._productID = newID