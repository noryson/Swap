class Membership:
    """ invariants:
    """

    _blocked: bool = False
    _chatID: int = None
    _participantID: int = None

    def block(self) -> None:
        self.setBlocked(True)

    def unblock(self) -> None:
        self.setBlocked(False)

    # helpers and checkers
    def isBlocked(self) -> bool:
        return self.getBlocked()

    # getters and setters
    def getBlocked(self) -> bool:
        return self._blocked

    def setBlocked(self, blocked: bool) -> None:
        self._blocked = bool

    def getChatID(self) -> int:
        return self._chatID

    def setChatID(self, chatID: int) -> None:
        self._chatID =chatID

    def getParticipantID(self) -> int:
        return self._participantID

    def setParticipantID(self, participantID: int) -> None:
        self._participantID = participantID
