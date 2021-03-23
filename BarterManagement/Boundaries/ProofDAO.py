from StorageManagement.Boundaries.DatabaseConnection import DatabaseConnection
from StorageManagement.Boundaries.DTO import DatabaseDTO
from BarterManagement.Entities.Proof import Proof

import sys
m = 'BarterManagement.Entities.OfferProxy'
if m not in sys.modules:
    import BarterManagement.Entities.OfferProxy as OfferProxyModule
else:
    OfferProxyModule = sys.modules['BarterManagement.Entities.OfferProxy']


class ProofDAO:

    """ invariants:
            @inv getDatabaseTable() = 'Barter'
            @inv getdbConnection() != None
        """
    databaseTable = 'Proof'
    dbConnection = None

    def __init__(self):
        self.dbConnection = DatabaseConnection()

    def create(self, ownerID: int, offerID: int, fileID: int) -> None:
        pass

    def get(self, proofID: int) -> Proof:
        proof: Proof = Proof()
        proof.setID(1)
        proof.setStatus('confirmed')

        offer: OfferProxyModule.OfferProxy = OfferProxyModule.OfferProxy()
        offer.setRealOfferID(1)
        proof.setOffer(offer)

        # file: 'FileProxy' = FileProxy()
        # file.setID(1)
        # proof.setFile(file)
        return proof

    def getAll(self) -> []:
        pass

    def find(self) -> None:
        pass

    def update(self, proof) -> None:
        pass

    def delete(self, proofID) -> None:
        print("proof deleted")
        pass