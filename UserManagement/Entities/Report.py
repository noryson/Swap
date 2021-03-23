import datetime


class Report:
    _complainantID: int = None
    _complaineeID: int = None
    _complaint: str = None
    _seen: bool = None
    _resolved: bool = None
    _dateCreated: datetime.datetime = None

    def seen(self) -> None:
        self._seen = True

    def unseen(self) -> None:
        self._seen = False

    def resolve(self) -> None:
        self._resolved = True

    def unresolve(self) -> None:
        self._resolved = False

    # helpers and checkers
    def isSeen(self) -> bool:
        return self.getSeen()

    def isResolved(self) -> bool:
        return self.getResolved()

    # getters and setters
    def getComplainantID(self) -> int:
        return self._complainantID

    def setComplainantID(self, complainantID: int) -> None:
        self._complainantID = complainantID

    def getComplaineeID(self) -> int:
        return self._complaineeID

    def setComplaineeID(self, complaineeID: int):
        self._complaineeID = complaineeID

    def getComplaint(self) -> str:
        return self._complaint

    def setComplaint(self, complaint: str) -> None:
        self._complaint = complaint

    def getSeen(self) -> bool:
        return self._seen

    def setSeen(self, seen: bool) -> None:
        self._seen = seen

    def getResolved(self) -> bool:
        return self._resolved

    def setResolved(self, resolved: bool) -> None:
        self._resolved = resolved

    def getDate(self) -> datetime.datetime:
        return self._dateCreated

    def setDate(self, date: datetime.datetime) -> None:
        self._dateCreated = date
