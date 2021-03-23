from BarterManagement.Entities.ProofAccess import ProofAccess
from BarterManagement.Entities.ProofProxy import ProofProxy
from BarterManagement.Boundaries.ProofDAO import ProofDAO
from Exceptions.ProofExceptions import *
from Exceptions.BarterExceptions import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BarterManagement.Entities.Proof import Proof


class DeleteTransferProofControl:
    """ invariants:
        @inv getProof() != None
    """

    _proof: ProofProxy = None

    def __init__(self, proofID) -> None:
        try:
            proofProxy: ProofProxy = ProofProxy()
            proofProxy.setRealProofID(proofID)
            proofProxy.proxyCheck()
            self._proof = proofProxy
        except ProofNotFoundException:
            raise RuntimeError()

    """ execute()
        @pre proof.getBarter().is[terminated, concluded] = False
        @pre proof.isConfirmed = False
    """
    def execute(self):
        try:
            barter = self.getProof().getOffer().getBarter()
            if barter.isDeactivated():
                raise BarterDeactivatedException(barter.getID())
            if barter.isConcluded():
                raise BarterConcludedException(barter.getID())
            if barter.isTerminated():
                raise BarterTerminatedException(barter.getID())

            if self.getProof().isConfirmed():
                raise ProofIsConfirmedException
        except BarterDeactivatedException:
            raise RuntimeError()
        except BarterConcludedException:
            raise RuntimeError()
        except BarterTerminatedException:
            raise RuntimeError()
        except ProofIsConfirmedException:
            raise RuntimeError()

        try:
            proof: ProofProxy = self.getProof()
            access: ProofAccess = ProofAccess(proof._realProof)
            if not access.isAccessible('delete'):
                raise PermissionError(access)
            proofDao: ProofDAO = ProofDAO()
            proofDao.delete(self.getProof().getID())
        except PermissionError:
            raise RuntimeError()

    def notifyInterestGroup(self):
        pass

    # getters and setters
    def getProof(self) -> ProofProxy:
        return self._proof

    def setProof(self, newProof: ProofProxy) -> None:
        self._proof = newProof