from BarterManagement.Entities.ProofProxy import ProofProxy
from BarterManagement.Boundaries.ProofDAO import ProofDAO
from Exceptions.ProofExceptions import *
from Exceptions.BarterExceptions import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BarterManagement.Entities.Proof import Proof


class DenyProofControl:
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
            pass

    """ execute()
        @pre proof.getBarter().is[terminated, concluded] = False
        @pre proof.isConfirmed = True
        @post proof.isConfirmed = False
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
            if not barter.isTransferring():
                raise BarterNotTransferringException

            if not self.getProof().isConfirmed():
                raise ProofNotConfirmedException
        except BarterDeactivatedException:
            pass
        except BarterConcludedException:
            pass
        except BarterTerminatedException:
            pass
        except BarterNotTransferringException:
            pass
        except ProofNotConfirmedException:
            pass

        try:
            self.getProof().deny()
        except PermissionError:
            pass

    def notifyIG(self):
        pass

    # getters and setters
    def getProof(self) -> ProofProxy:
        return self._proof

    def setProof(self, newProof: ProofProxy) -> None:
        self._proof = newProof