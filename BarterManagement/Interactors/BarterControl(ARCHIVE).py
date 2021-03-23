from StoreManagement.Entities.Product import Product
from StoreManagement.Entities.Store import Store

class BarterControl:
    """ invariants:
        @inv StoreManagement.isProductExisting(product) = True
        @inv StoreManagement.isStoreExisting(store)
        @inv product.getStore() = getStore()
        @inv store.getProducts() contains product
        @inv getMaxNoOfBarters() > 0
        @inv getBarter() != None, getProduct() != None, getStore() != None
    """
    # todo: design patterns[facade, proxy, DAOs, bridge/factory, composite, observer, control_flow] DONE
    # todo: access control DONE
    # todo: storage DONE
    # todo: inheritance DONE
    # todo: associations DONE
    # todo: exception
    # todo: optimization
    # TODO: Make DAOs.create return the id of new item just created
    product = None
    store = None
    barter = None
    seller = None
    maxNoOfBarters = None
    maxNoOfOffers = None
    maxNoOfProofs = None
    noOfSellersProof = None
    noOfBuyersProof = None
    fileExtension = []

    # getters and setters omitted

    def __init__(self, productID):
        pass

    """ createBarter(endDate)
        @pre product.getSeller() = barterDTO.getSeller()
        @pre isSellerOverbooked() = False
        @pre barter = None
        @pre endDate > presentDate by 1 week
        @post barter != None
        @post seller.getNoOfBarters() = seller.getNoOfBarters() + 1
    """
    def createBarter(self, endDate):
        pass

    """ notifySubscribers(subscribers)
       @pre Barter.getProduct().getStore().getSuscribers() != None
       @pre Barter.getProduct().isAnnounced() = False
       @post Barter.getProduct().isAnnounced() = True
    """
    def notifySubscribers(self):
        pass

    """ terminateBarter()
        @pre getBarter().isConcluded() = False
        @pre getBarter().isTransferring = False
        @post getBarter() = None
    """
    def terminateBarter(self):
        pass

    """ notifyBuyersOfBarterTermination()
        @pre getBarter().getOffers() != None
    """
    def notifyBuyersOfBarterTermination(self, barter):
        pass

    """ makeOffer(offerDTO)
        @pre offerDTO.buyer != product.getSeller()
        @pre barter.isConcluded() = False
        @pre barter.isTransferring = False
        @pre barter.getOffers().buyer !contain offerDTO.buyer
        @post barter.getOffers() contain offerDTO 
        @post barter.isTransferring = True
    """
    def makeOffer(self, offerDTO):
        pass

    """ notifySellerOfNewOffer(offer)
        @pre barter.getOffers() contains offer
    """
    def notifySellerOfNewOffer(self, offer):
        pass

    """ withdrawOffer(offer)
        @pre barter.getOffers() contains offer
        @pre user = offer.getSeller()
        @pre barter.isConcluded() = False
        @pre barter.isTransferring = False
        @post barter.getOffers() !contain offer
        @post barter.getNoOfOffers() = barter.getNoOfOffers() - 1
    """
    def withdrawOffer(self, offer):
        pass

    def notifyOwnerOfWithdrawal(self, offer):
        pass

    def getAllOffers(self):
        pass

    def getOffer(self, offerID):
        pass

    """ acceptOffer(offer)
       @pre isTransferring() = False
       @post isTransferring() = True
    """
    def acceptOffer(self, offer):
        pass

    """ notifyBuyerOfAcceptance(offer)
        @pre offer.isTransferring() = True
    """
    def notifyBuyerOfAcceptance(self, offer):
        pass

    """" rejectOffer(offer)
        @pre offer.isTransferring() = True
        @pre offer.hasProof() = False
        @post offer.isTransferring() = False
    """
    def rejectOffer(self, offer):
        pass

    """ notifyBuyerOfRejection(offer)
        @pre offer.isTransferring() = False
    """
    def notifyBuyerOfRejection(self, offer):
        pass

    """ createProof(proofDTO)
        @pre barter.isTransferring() = True
        @pre proofDTO.getOffer() = barter.getAcceptedOffer()
        @pre proofDTO.getOwner() = getSeller() | barter.getAcceptedOffer().getBuyer()
        @pre barter.getNoOfOwnerProof() < getMaxNoOfOwnersProof()
        @pre getFileExtension() contains proofDTO.fileExtension 
        @post barter.getNoOfOwnerProof() = barter.getNoOfOwnerProof() + 1
    """
    def createProof(self, proofDTO):
        pass

    """ notifyForProof(proof)
        @pre offer.hasProof() = True
    """
    def notifyForProof(self, proof):
        pass

    def getAllProof(self):
        pass

    def getProof(self, proofID):
        pass

    """ deleteProof(proof)
        @pre barter.isTransferring() = True
        @pre barter.getProof() contains proof
        @pre barter.isConcluded() = False
        @pre proof.isConfirmed() = False
        @post barter.getProof !contain proof
    """
    def deleteProof(self, proof):
        pass

    """ notifyUserOfDeletedProof(offer)
        @pre 
    """
    def notifyUserOfDeletedProof(self, proof):
        pass

    """ confirmProof(proof)
        @pre proof.isConfirmed() = False
        @pre user = proof.getBarter().getBuyer() | proof.getBarter().getSeller()
        @post proof.isConfirmed() = True
    """
    def confirmProof(self, proof):
        pass

    def isBuyerOverbooked(self, buyer):
        pass