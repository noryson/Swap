import datetime


class Message:
    """ invariants:
    """

    _messageID: int = None
    _information: str = None
    _senderMemberShipID: int = None
    _read: bool = False
    _creationDate: datetime.datetime = None
    _chatID: int = None
    _deleted: bool = False

    def read(self) -> None:
        self.setRead(True)

    def unread(self) -> None:
        self.setRead(False)

    def delete(self) -> None:
        self.setDeleted(True)

    # helpers and checkers
    def isRead(self) -> bool:
        return self.getRead()

    def isDeleted(self) -> bool:
        return self.getDeleted()

    # getters and setters
    def getRead(self) -> bool:
        return self._read

    def setRead(self, read: bool) -> bool:
        self._read = read

    def getDeleted(self) -> bool:
        return self._deleted

    def setDeleted(self, deleted: bool) -> None:
        self._deleted = deleted

    def getID(self) -> int:
        return self._messageID

    def setID(self, messageID: int) -> None:
        self._messageID = messageID

    def getInformation(self) -> str:
        return self._information

    def setInformation(self, information: str) -> None:
        self._information = information

    def getSenderMembershipID(self) -> int:
        return self._senderMemberShipID

    def setSenderMembershipID(self, membershipID: int) -> None:
        self._senderMemberShipID = membershipID

    def getDate(self) -> datetime.datetime:
        return self._creationDate

    def setDate(self, date: datetime.datetime) -> None:
        self._creationDate = date

    def getChatID(self) -> int:
        return self._chatID

    def setChatID(self, chatID) -> None:
        self._chatID = chatID
