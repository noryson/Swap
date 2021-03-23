class Chat:
    """ invariants:
    """

    _messageIDs: [] = list()
    _membershipIDs: [] = list()
    _type: str = 'private'
    _replyable: bool = False

    def makeReplyable(self) -> None:
        self.setReplyable(True)

    def makeUnreplyable(self) -> None:
        self.setReplyable(False)

    # helpers and checker
    def isReplyable(self):
        return self.getReplyable()

    def getNoOfMessages(self) -> int:
        return len(self.getMessageIDs())

    def getNoOfMembers(self) -> int:
        return len(self.getMembershipIDs())

    # getters and setters
    def getMessageIDs(self) -> []:
        return self._messageIDs

    def setMessageIDs(self, messageIDs: []) -> None:
        self._messageIDs = messageIDs

    def getMembershipIDs(self) -> []:
        return self._membershipIDs

    def setMembershipIDs(self, membershipIDs) -> None:
        self._membershipIDs = membershipIDs

    def getReplyable(self) -> bool:
        return self._replyable

    def setReplyable(self, replyable: bool) -> None:
        self._replyable =replyable

    def getType(self) -> str:
        return self._type

    def setType(self, type: str) -> None:
        self._type = type
