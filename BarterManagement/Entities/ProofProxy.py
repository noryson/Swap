import datetime
from BarterManagement.Entities.ProofAccess import ProofAccess
from Exceptions.ProofExceptions import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BarterManagement.Entities.Proof import Proof
    from BarterManagement.Entities.FileProxy import FileProxy
    from BarterManagement.Entities.OfferProxy import OfferProxy


class ProofProxy:
    """ invariants:
        @inv
    """

    _realProofID: int = None
    _realProof: 'Proof' = None
    _access: 'ProofAccess' = None

    # ProofProxy calls
    def proxyCheck(self) -> None:
        if self._realProof is None:
            try:
                from BarterManagement.Boundaries.ProofDAO import ProofDAO
                proofDao = ProofDAO()
                self._realProof = proofDao.get(self._realProofID)
                self._access = ProofAccess(self._realProof)
            except ProofNotFoundException(self):
                pass

    def getRealProofID(self) -> int:
        return self._realProofID

    def setRealProofID(self, newID: int) -> None:
        self._realProofID = newID

    # main Proof calls
    def confirm(self) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('confirm'):
            raise PermissionError(self._access)
        else:
            self._realProof.confirm()

    def deny(self) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('deny'):
            raise PermissionError(self._access)
        else:
            self._realProof.deny()

    # checkers and helpers
    def isConfirmed(self) -> bool:
        self.proxyCheck()
        return self._realProof.isConfirmed()

    # getters and setters
    def getID(self) -> int:
        self.proxyCheck()
        return self._realProof.getID()

    def setID(self, newID) -> None:
        self.proxyCheck()
        self._realProof.setID(newID)

    def getDate(self) -> datetime:
        self.proxyCheck()
        return self._realProof.getDate()

    def setDate(self, newDate: datetime.datetime) -> None:
        self.proxyCheck()
        self._realProof.setDate(newDate)

    def getOffer(self) -> 'OfferProxy':
        self.proxyCheck()
        return self._realProof.getOffer()

    def setOffer(self, newOffer: 'OfferProxy') -> None:
        self.proxyCheck()
        self._realProof.setOffer(newOffer)

    def getFile(self) -> 'FileProxy':
        self.proxyCheck()
        return self._realProof.getFile()

    def setFile(self, newFile: 'FileProxy') -> None:
        self.proxyCheck()
        self._realProof.setFile(newFile)

    def getStatus(self) -> str:
        self.proxyCheck()
        return self._realProof.getStatus()

    def setStatus(self, newStatus: str) -> None:
        self.proxyCheck()
        self._realProof.setStatus(newStatus)