import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BarterManagement.Entities.OfferProxy import OfferProxy
    from BarterManagement.Entities.FileProxy import FileProxy
from Exceptions.ProofExceptions import *


class Proof:
    """ invariants:
        @inv all fields must be filled
        @inv getStatus() = ['confirmed','denied']
    """
    _proofID: int = None
    _owner: int = None
    _status: str = None
    _creationDate: datetime.datetime = None
    _offer: 'OfferProxy' = None
    _file: ['FileProxy'] = None

    """ confirm()
        @pre isConfirmed == False
        @post isConfirmed == True
    """
    def confirm(self) -> None:
        if not self.isConfirmed():
            self.setStatus('confirmed')
            self.synchronizeDB()

    """ deny()
        @pre isConfirmed() == True
        @post isConfirmed() == False
    """
    def deny(self) -> None:
        if self.isConfirmed():
            self.setStatus('denied')
            self.synchronizeDB()

    # checkers and helpers
    def isConfirmed(self) -> bool:
        if self.getStatus() == 'confirmed':
            return True
        else:
            return False

    def synchronizeDB(self) -> None:
        from BarterManagement.Boundaries.ProofDAO import ProofDAO

        dao: ProofDAO = ProofDAO()
        dao.update(self)

    # getters and setters
    def getID(self) -> int:
        return self._proofID

    def setID(self, newID: int) -> None:
        self._proofID = newID

    def getDate(self) -> datetime:
        return self._creationDate

    def setDate(self, newDate: datetime.datetime) -> None:
        self._creationDate = newDate

    def getOffer(self) -> 'OfferProxy':
        return self._offer

    def setOffer(self, newOffer: 'OfferProxy') -> None:
        self._offer = newOffer

    def getFile(self) -> 'FileProxy':
        return self._file

    def setFile(self, newFile: 'FileProxy') -> None:
        self._file = newFile

    def getStatus(self) -> str:
        return self._status

    def setStatus(self, newStatus: str) -> None:
        self._status = newStatus
