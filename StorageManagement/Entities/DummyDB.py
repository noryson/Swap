import datetime
from StorageManagement.Entities.DatabaseInterface import DatabaseInterface
from Exceptions.DatabaseExceptions import *


class DummyDB(DatabaseInterface):
    BarterTable = list()
    OfferTable = list()
    ProofTable = list()

    def open(self):
        pass

    def close(self):
        pass

    def create(self, data) -> int:
        if data.table == 'Barter':
            barter = dict()
            barter['ID'] = len(self.BarterTable) + 1
            barter['requestedItem'] = data.requestedItem
            barter['maxNoOfOffers'] = 20
            barter['endDate'] = data.endDate
            barter['status'] = 'running'
            barter['adminStatus'] = 'active'
            barter['productID'] = 1

            self.BarterTable.append(barter)
            print("Barter created")
            return barter['ID']

        if data.table == 'Offer':
            offer = dict()
            offer['ID'] = len(self.OfferTable) + 1
            offer['offeredProduct'] = data.offeredProduct
            offer['status'] = 'active'
            offer['creationDate'] = datetime.datetime.now()
            offer['barterID'] = data.barterID
            offer['buyerID'] = data.buyerID

            self.OfferTable.append(offer)
            print("Offer created")
            return offer['ID']

        if data.table == 'Proof':
            proof = dict()
            proof['ID'] = len(self.OfferTable) + 1
            proof['offerID'] = data.offerID
            proof['fileID'] = data.fileID

            self.ProofTable.append(proof)
            print('Proof created')
            return proof['ID']

    def get(self, data):
        if data.table == 'Barter':
            for b in self.BarterTable:
                if b['ID'] == data.ID:
                    offerIDs = list()
                    for offer in self.OfferTable:
                        if offer['barterID'] == b['ID']:
                            offerIDs.append(offer['ID'])

                    result = dict()
                    result['ID'] = b['ID']
                    result['requestedItem'] = b['requestedItem']
                    result['maxNoOfOffers'] = b['maxNoOfOffers']
                    result['endDate'] = b['endDate']
                    result['status'] = b['status']
                    result['adminStatus'] = b['adminStatus']
                    result['offerIDs'] = offerIDs
                    result['productID'] = b['productID']
                    return result
            raise DBEntryNotFoundException

        if data.table == 'Offer':
            for o in self.OfferTable:
                if o['ID'] == data.ID:
                    proofIDs = list()
                    for proof in self.ProofTable:
                        if proof['barterID'] == o['ID']:
                            proofIDs.append(proof['ID'])

                    result = dict()
                    result['ID'] = o['ID']
                    result['offeredProduct'] = o['offeredProduct']
                    result['status'] = o['status']
                    result['creationDate'] = o['creationDate']
                    result['barterID'] = o['barterID']
                    result['buyerID'] = o['buyerID']
                    result['proofIDs'] = proofIDs
                    return result
            raise DBEntryNotFoundException

        if data.table == 'Proof':
            for p in self.ProofTable:
                if p['ID'] == data.ID:
                    return p
            raise DBEntryNotFoundException

    def find(self, data):
        if data.table == 'Barter':
            result: [] = list()
            for barter in self.BarterTable:
                if barter['requestedItem'] == data.requestedItem[1] \
                    and barter['status'] == data.status[1] and barter['adminStatus'] == data.adminStatus[1]: # fully implement all data search items
                    result.append(barter)
            if len(result) > 0:
                return result
            else:
                raise DBEntryNotFoundException

        if data.table == 'Offer':
            pass

        if data.table == 'Proof':
            pass

    def update(self, data):
        if data.table == 'Barter':
            inc: int = 0
            for b in self.BarterTable:
                if b['ID'] == data.ID:
                    b['requestedItem'] = data.requestedItem
                    b['maxNoOfOffers'] = data.maxNoOfOffers
                    b['endDate'] = data.endDate
                    b['status'] = data.status
                    b['adminStatus'] = data.adminStatus
                    # b['productID'] = data.productID

                    self.BarterTable[inc] = b
                    print("Barter updated")
                    return
                inc += 1
            raise DBUpdateFailException(data)

        if data.table == 'Offer':
            inc: int = 0
            for offer in self.OfferTable:
                if offer['ID'] == data.ID:
                    offer['offeredProduct'] = data.offeredProduct
                    offer['status'] = data.status
                    # offer['creationDate'] = data.creationDate
                    offer['barterID'] = data.barterID
                    # offer['buyerID'] = data.buyerID

                    self.OfferTable[inc] = offer
                    print('Offer updated')
                    return
                inc += 1
            raise DBUpdateFailException(data)

        if data.table == 'Proof':
            inc: int = 0
            for proof in self.ProofTable:
                if proof['ID'] == data.ID:
                    proof['offerID'] = data.offerID
                    proof['fileID'] = data.fileID

                    self.ProofTable[inc] = proof
                    print('Proof updated')
                    return
                inc += 1
            raise DBUpdateFailException(data)

    def delete(self, data):
        if data.table == 'Barter':
            inc: int = 0
            for b in self.BarterTable:
                if b['ID'] == data.ID:
                    self.BarterTable.pop(inc)
                    print("Barter deleted")
                    return
                inc += 1
            raise DBEntryDeletionFailException(data)

        if data.table == 'Offer':
            inc: int = 0
            for b in self.OfferTable:
                if b['ID'] == data.ID:
                    self.OfferTable.pop(inc)
                    print("Offer deleted")
                    return
                inc += 1
            raise DBEntryDeletionFailException(data)

        if data.table == 'Proof':
            inc: int = 0
            for b in self.ProofTable:
                if b['ID'] == data.ID:
                    self.ProofTable.pop(inc)
                    print("Proof deleted")
                    return
                inc += 1
            raise DBEntryDeletionFailException(data)
