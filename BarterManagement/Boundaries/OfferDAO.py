import datetime
from StorageManagement.Boundaries.DatabaseConnection import DatabaseConnection
from StorageManagement.Boundaries.DTO import DatabaseDTO
import StorageManagement.Entities.Cache as cache
import sys
m = 'BarterManagement.Entities.BarterProxy'
if m not in sys.modules:
    import BarterManagement.Entities.BarterProxy as BarterProxyModule
else:
    BarterProxyModule = sys.modules['BarterManagement.Entities.BarterProxy']

m = 'BarterManagement.Entities.ProofProxy'
if m not in sys.modules:
    import BarterManagement.Entities.ProofProxy as ProofProxyModule
else:
    ProofProxyModule = sys.modules['BarterManagement.Entities.ProofProxy']

m = 'UserManagement.Entities.UserProxy'
if m not in sys.modules:
    import UserManagement.Entities.UserProxy as UserProxyModule
else:
    UserProxyModule = sys.modules['UserManagement.Entities.UserProxy']

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    pass
    # from BarterManagement.Entities.BarterProxy import BarterProxy
    # from BarterManagement.Entities.ProofProxy import ProofProxy
    # from UserManagement.Entities.UserProxy import UserProxy
from BarterManagement.Entities.Offer import Offer
from Exceptions.OfferExceptions import *
from Exceptions.DatabaseExceptions import *


class OfferDAO:
    """ invariants:
                @inv getDatabaseTable() = 'Barter'
                @inv getdbConnection() != None
            """
    databaseTable = 'Offer'
    dbConnection = None

    def __init__(self):
        self.dbConnection = DatabaseConnection('test')

    def create(self, offeredProduct: str, barterID: int, buyerID: int) -> int:
        data = type('dto', (object,), {})()
        data.offeredProduct = offeredProduct
        data.barterID = barterID
        data.buyerID = buyerID
        data.table = self.databaseTable

        try:
            newID = self.dbConnection.create(data)
        except DBEntryCreationFailException(data):
            raise OfferCreationFailedException(data)

        cache.invalidate()
        return newID
        # db = self.dbConnection
        # data = {'table': self.databaseTable, 'offeredProduct': offeredProduct, 'barterID': barterID, 'buyerID': buyerID}
        # newID = db.create(data)
        #
        # # Updating dummyDB for barter with new offerID
        # from BarterManagement.Entities.OfferProxy import OfferProxy
        # offerProxy = OfferProxy()
        # offerProxy.setRealOfferID(newID)
        #
        # from BarterManagement.Entities.BarterProxy import BarterProxy
        # barterProxy = BarterProxy()
        # barterProxy.setRealBarterID(barterID)
        # barterProxy.setOffers(barterProxy.getOffers().append(offerProxy))
        # barterProxy._realBarter.synchronizeDB()

    def get(self, offerID: int) -> Offer:
        if cache.isCached(self.databaseTable, offerID):
            return cache.get(self.databaseTable, offerID)

        data = type('dto', (object,), {})()
        data.table = self.databaseTable
        data.ID = offerID

        try:
            o = self.dbConnection.get(data)
        except DBEntryNotFoundException:
            raise OfferNotFoundException(data)

        offer = Offer()
        offer.setID(o['ID'])
        offer.setOfferedProduct(o['offeredProduct'])
        offer.setDate(o['creationDate'])
        offer.setStatus(o['status'])

        barter = BarterProxyModule.BarterProxy()
        barter.setRealBarterID(o['barterID'])
        offer.setBarter(barter)

        proofs: [ProofProxyModule] = list()
        for proofID in o['proofIDs']:
            proof: ProofProxyModule = ProofProxyModule.ProofProxy()
            proof.setRealProofID(proofID)
            proofs.append(proof)
        offer.setProofs(proofs)

        # buyer: UserProxyModule.UserProxy = UserProxyModule.UserProxy()
        # buyer.setRealBuyerID(1)
        # offer.setBuyer(buyer)

        cache.save(self.databaseTable, offerID, offer)
        return offer

    def getAll(self) -> []:
        pass

    def find(self) -> None:
        pass

    def update(self, offerUpdate: Offer) -> None:
        data = type('dto', (object,), {})()
        data.table = self.databaseTable
        data.ID = offerUpdate.getID()
        data.offeredProduct = offerUpdate.getOfferedProduct()
        data.status = offerUpdate.getStatus()
        data.barterID = offerUpdate.getBarter().getID()
        data.buyerID = 1  # offerUpdate.getBuyer().getID()

        try:
            self.dbConnection.update(data)
        except DBUpdateFailException:
            raise OfferUpdateFailedException(offerUpdate)

        cache.invalidate()

    def delete(self, offerID) -> None:
        data = type('dto', (object,), {})()
        data.table = self.databaseTable
        data.ID = offerID

        try:
            self.dbConnection.delete(data)
        except DBEntryDeletionFailException:
            raise OfferDeleteFailedException(offerID)

        cache.invalidate()
