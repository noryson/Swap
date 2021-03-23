import datetime
from StorageManagement.Boundaries.DatabaseConnection import DatabaseConnection
import StorageManagement.Entities.Cache as cache
from StorageManagement.Boundaries.DTO import DatabaseDTO
import sys
# m = 'BarterManagement.Entities.OfferProxy'
# if m not in sys.modules:
#     from BarterManagement.Entities.OfferProxy import OfferProxy
# else:
#     OfferProxy = sys.modules['BarterManagement.Entities.OfferProxy']
m = 'BarterManagement.Entities.OfferProxy'
if m not in sys.modules:
    import BarterManagement.Entities.OfferProxy as OfferProxyModule
else:
    OfferProxyModule = sys.modules['BarterManagement.Entities.OfferProxy']
from BarterManagement.Entities.Barter import Barter
from Exceptions.BarterExceptions import BarterNotFoundException, BarterUpdateFailException, BarterDeleteFailException, \
    BarterCreationFailException
from Exceptions.DatabaseExceptions import *


class BarterDAO:

    """ invariants:
        @inv getDatabaseTable() = 'Barter'
        @inv getdbConnection() != None
    """
    databaseTable = 'Barter'
    dbConnection = None

    def __init__(self):
        self.dbConnection = DatabaseConnection('test')

    """ create(barterDTO)
        @pre barterDTO.getProduct().getBarter() = None or product.canHostBarter = True
        @pre barterDTO.getProduct().getBarter() != None
    """
    def create(self, productID: int, requestedItem: str, endDate: datetime.datetime):
        data = type('dto', (object,), {})()
        data.productID = productID
        data.requestedItem = requestedItem
        data.endDate = endDate
        data.table = self.databaseTable

        try:
            newID = self.dbConnection.create(data)
        except DBEntryCreationFailException:
            raise BarterCreationFailException(data)

        cache.invalidate()
        return newID

    """ get(barterDTO)
        @pre barterDTO.getID() != None
    """
    def get(self, barterID: int) -> Barter:
        if cache.isCached(self.databaseTable, barterID):
            return cache.get(self.databaseTable, barterID)

        data = type('dto', (object,), {})()
        data.table = self.databaseTable
        data.ID = barterID

        try:
            b = self.dbConnection.get(data)
        except DBEntryNotFoundException:
            raise BarterNotFoundException(barterID)

        barter = Barter()
        barter.setID(b['ID'])
        barter.setRequest(b['requestedItem'])
        barter.setMaxNoOfOffers(b['maxNoOfOffers'])
        barter.setEndDate(b['endDate'])
        barter.setStatus(b['status'])
        barter.setAdminStatus(b['adminStatus'])

        offers: ['OfferProxyModule.OfferProxy'] = list()
        for offerID in b['offerIDs']:
            offer: OfferProxyModule.OfferProxy = OfferProxyModule.OfferProxy()
            offer.setRealOfferID(offerID)
            offers.append(offer)
        barter.setOffers(offers)

        # product: ProductProxy = ProductProxy()
        # product.setRealProductID(1)
        # barter.setProduct(product)

        cache.save(self.databaseTable, barterID, barter)
        return barter

    """ search(barterDTO)
        @pre barterDTO != empty
    """
    def find(self, productName, requestedItem=None, category=None, limit=30, page=1, status=None, adminStatus=None,
             sort=None, order=None, startDate: datetime.datetime = None, endDate: datetime.datetime = None) -> []:
        data = type('dto', (object,), {})()
        data.table = self.databaseTable
        data.productName = ('like', productName)
        data.requestedItem = ('like', requestedItem)
        data.category = ('equals', category)
        data.limit = ('equals', limit)
        data.page = ('equals', page)
        data.status = ('equals', status)
        data.adminStatus = ('equals', adminStatus)
        data.sort = ('equals', sort)
        data.order = ('equals', order)
        data.startDate = ('greater than', startDate)
        data.endDate = ('lesser than', endDate)

        try:
            result: [] = self.dbConnection.find(data)
        except DBEntryNotFoundException:
            raise BarterNotFoundException

        return result

    """ update(barterDTO)
        @pre barterDTO.getID() != None
    """
    def update(self, barter: Barter) -> None:
        data = type('dto', (object,), {})()
        data.table = self.databaseTable
        data.ID = barter.getID()
        data.requestedItem = barter.getRequest()
        data.maxNoOfOffers = barter.getMaxNoOfOffers()
        data.endDate = barter.getEndDate()
        data.status = barter.getStatus()
        data.adminStatus = barter.getAdminStatus()
        # data.productID = barter.getProduct().getID()

        try:
            self.dbConnection.update(data)
        except DBUpdateFailException:
            raise BarterUpdateFailException(barter)

        cache.invalidate()

    """ delete(barterDTO)
        @pre barterDTO.getID() != None
    """
    def delete(self, barterID) -> None:
        data = type('dto', (object,), {})()
        data.ID = barterID

        try:
            self.dbConnection.delete(data)
        except DBEntryDeletionFailException:
            raise BarterDeleteFailException(barterID)

        cache.invalidate()

