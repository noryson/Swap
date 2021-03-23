import datetime
from UserManagement.Entities.Privilege import Privilege
from UserManagement.Entities.Report import Report
from Exceptions.UserExceptions import *


class User:
    _ID: int = None
    _firstName: str = None
    _lastName: str = None
    _email: str = None
    _online: bool = False
    _role: str = 'user'
    _secret: str = None
    _active: bool = None
    _verified: bool = None
    _verificationToken: str = None
    _dateRegistered: datetime.datetime = None
    _lastLogin: datetime.datetime = None
    _storeID: int = None
    _reports: [Report] = None
    _profileImageID: int = None
    _chatIDs: [] = None
    _subscribedStoreIDs: [int] = None
    _groups: [] = None

    def login(self) -> None:
        pass

    def logout(self) -> None:
        pass

    def changeSecret(self, secret: str) -> None:
        pass

    def changeProfileImage(self, imageID: int) -> None:
        pass

    def changeRole(self, role: str) -> None:
        pass

    def deactivate(self) -> None:
        pass

    def activate(self) -> None:
        pass

    def updateLastLogin(self, lastLogin: datetime.datetime) -> None:
        pass

    def verify(self, token: str) -> None:
        if self.isVerified():
            raise UserIsVerifiedException

        if self.getVerificationToken() != token:
            raise UserVerificationFailedException

        self.setVerified(True)

    # helpers and checkers
    def isActive(self) -> bool:
        pass

    def isVerified(self) -> bool:
        return self.getVerified()

    def isOnline(self) -> bool:
        pass

    def isStaff(self) -> bool:
        pass

    def getNoOfReports(self) -> int:
        return len(self.getReports())

    def getNoOfChats(self) -> int:
        return len(self.getChatIDs())

    def getNoOfSubscriptions(self) -> int:
        return len(self.getSubscriptionIDs())

    def synchronizeDB(self) -> None:
        pass

    # getters and setter
    def getID(self) -> int:
        return self._ID

    def setID(self, userID: int) -> None:
        self._ID = userID

    def getFirstName(self) -> str:
        return self._firstName

    def setFirstName(self, firstName: str) -> None:
        self._firstName = firstName

    def getLastName(self) -> str:
        return self._lastName

    def setLastName(self, lastName: str) -> None:
        self._lastName = lastName

    def getEmail(self) -> str:
        return self._email

    def setEmail(self, email) -> None:
        self._email = email

    def getOnline(self) -> bool:
        return self._online

    def setOnline(self, online: bool) -> None:
        self._online = online

    def getRole(self) -> str:
        return self._role

    def setRole(self, role: str) -> None:
        self._role = role

    def getSecret(self) -> str:
        return self._secret

    def setSecret(self, secret: str) -> None:
        self._secret = secret

    def getActive(self) -> bool:
        return self._active

    def setActive(self, active) -> None:
        self._active = active

    def getDate(self) -> datetime.datetime:
        return self._dateRegistered

    def setDate(self, date: datetime.datetime) -> None:
        self._dateRegistered = date

    def getStoreID(self) -> int:
        return self._storeID

    def setStoreID(self, storeID: int) -> None:
        self._storeID = storeID

    def getReports(self) -> []:
        return self._reports

    def setReports(self, reports: []) -> None:
        self._reports = reports

    def getProfileImageID(self) -> int:
        return self._profileImageID

    def setProfileImageID(self, imageID: int) -> None:
        self._profileImageID = imageID

    def getChatIDs(self) -> []:
        return self._chatIDs

    def setChatIDs(self, chatIDs: []) -> None:
        self._chatIDs = chatIDs

    def getSubscriptionIDs(self) -> []:
        return self._subscribedStoreIDs

    def setSubscriptionIDs(self, subscriptionIDs: []) -> None:
        self._subscribedStoreIDs = subscriptionIDs

    def getGroups(self) -> []:
        return self._groups

    def setGroups(self, groups: []) -> None:
        self._groups = groups

    def getLastLogin(self) -> datetime.datetime:
        return self._lastLogin

    def setLastLogin(self, lastLogin: datetime.datetime) -> None:
        self._lastLogin = lastLogin

    def getVerified(self) -> bool:
        return self._verified

    def setVerified(self, verified: bool) -> None:
        self._verified = verified

    def getVerificationToken(self) -> str:
        return self._verificationToken

    def setVerificationToken(self, token: str) -> None:
        self._verificationToken = token

