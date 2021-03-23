from BarterManagement.Entities.ProofProxy import ProofProxy
from BarterManagement.Boundaries.ProofDAO import ProofDAO
from Exceptions.ProofExceptions import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BarterManagement.Entities.Proof import Proof


class GetProofControl:
    """ invariants:
        @inv proof != None
    """

    _proof: ProofProxy = None

    def __init__(self, proofID: int) -> None:
        # This could as well be converted to a dto if it is for the UI
        try:
            proofDao: ProofDAO() = ProofDAO()
            proof: Proof = proofDao.get(proofID)
            proofProxy: ProofProxy = ProofProxy()
            proofProxy.setRealProofID(proof.getID())
            proofProxy._realProof = proof
            self._proof = proofProxy
        except ProofNotFoundException:
            raise RuntimeError()

    def execute(self) -> ProofProxy:
        return self._proof
