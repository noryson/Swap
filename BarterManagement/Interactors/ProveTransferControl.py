from BarterManagement.Boundaries.ProofDAO import ProofDAO
from BarterManagement.Boundaries.OfferDAO import OfferDAO
from BarterManagement.Entities.OfferProxy import OfferProxy
from BarterManagement.Entities.OfferAccess import OfferAccess
from FileManagement.Boundaries.Uploader import ProofUploader
from UserManagement.Boundaries.CurrentUserService import CurrentUserService
from Exceptions.OfferExceptions import *
from Exceptions.ProofExceptions import *
from Exceptions.BarterExceptions import *
from Exceptions.FileExceptions import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BarterManagement.Entities.Offer import Offer
    from FileManagement.Boundaries.FileDTO import FileDTO


class ProveTransferControl:
    """ invariants:
        @inv maxNoOfProofs > 0
        @inv offer.getNoOfBuyersProof() < maxNoOfProofs
        @inv offer.getNoOfSellersProof() < maxNoOfProofs
        @inv filename.extension included in fileExtensions
        @inv all fields != None
    """

    _maxNoOfProofs: int = None
    _offer: OfferProxy = None
    _fileDTO: FileDTO = None

    def __init__(self, offerID: int, file: FileDTO):
        try:
            offerProxy: OfferProxy = OfferProxy()
            offerProxy.setRealOfferID(offerID)
            offerProxy.proxyCheck()
            self.setOffer(offerProxy)

            self._fileDTO = file  # check file first
        except OfferNotFoundException:
            raise RuntimeError()

    """ execute()
        @pre offer.barter.isConcluded() = False
        @pre offer.barter.isTransferring() = True
        @pre offer.isAccepted() = True
        @pre getNoOfProof() < getMaxProof()
            @pre getOwnerNoOfProof < getMaxNoOfProof
            @pre getBuyerNoOfProof < getMaxNoOfProof
        @pre fileDTO.isValid() = True
        @pre currentUser = offer.buyer or offer.barter.product.store.owner
    """
    def execute(self):
        try:
            barter = self.getOffer().getBarter()
            if barter.isDeactivated():
                raise BarterDeactivatedException
            if barter.isConcluded():
                raise BarterConcludedException
            if barter.isTerminated():
                raise BarterTerminatedException
            if not self.getOffer().isAccepted():
                raise OfferNotAcceptedException

            offer: OfferProxy = self.getOffer()
            access: OfferAccess = OfferAccess(offer._realOffer)
            if not access.isAccessible('proveTransfer'):
                raise PermissionError(access)

            if self.getBuyerNoOfProof() > self.getMaxNoOfProofs():
                raise ProofMaxExceededException(offer)
            if self.getOwnerNoOfProof() > self.getMaxNoOfProofs():
                raise ProofMaxExceededException(offer)

        except BarterDeactivatedException:
            raise RuntimeError()
        except BarterConcludedException:
            raise RuntimeError()
        except BarterTerminatedException:
            raise RuntimeError()
        except OfferNotAcceptedException:
            raise RuntimeError()
        except PermissionError:
            raise RuntimeError()
        except ProofMaxExceededException:
            raise RuntimeError()

        try:
            uploader: ProofUploader = ProofUploader(self._fileDTO)
            uploader.upload()

            userService = CurrentUserService()
            currentUserID = userService.getCurrentUserID()

            proofDao = ProofDAO()
            proofDao.create(currentUserID, self.getOffer().getID(), uploader.getFileID())
        except FileNotFoundError:
            raise RuntimeError()
        except FileExistsError:
            raise RuntimeError()
        except FileTooLargeException:
            raise RuntimeError()
        except FileExtentionException:
            raise RuntimeError()

    def notifyInterestGroup(self):
        pass

    # getters and setters
    def getMaxNoOfProofs(self) -> int:
        return self._maxNoOfProofs

    def setMaxNoOfProofs(self, newMax) -> None:
        self._maxNoOfProofs = newMax

    def getOffer(self) -> OfferProxy:
        return self._offer

    def setOffer(self, newOffer: OfferProxy) -> None:
        self._offer = newOffer

    def getOwnerNoOfProof(self) -> int:
        pass

    def getBuyerNoOfProof(self) -> int:
        pass