import datetime
from UserManagement.Entities.DjangoGroup import DjangoGroup
from UserManagement.Entities.Report import Report
from django.contrib.auth.models import User
from UserManagement.Entities.User import User as SwapUser
from Exceptions.UserExceptions import *


class DjangoUser(SwapUser):
    _role: str = 'user'
    _reports: [Report] = None
    _profileImageID: int = None
    _chatIDs: [int] = None
    _subscribedStoreIDs: [int] = None
    _groups: [DjangoGroup] = None

    _user: User = None

    """ login()
        @pre isActive() == True
        @pre isOnline() == False
    """
    def login(self) -> None:
        if not self.isActive():
            raise UserIsInactiveException(self)
        if self.isOnline():
            raise UserIsOnlineException(self)

        self.setOnline(True)
        self.synchronizeDB()

    """ logout()
        @pre isActive() == True
        @pre isOnline() == True
    """
    def logout(self) -> None:
        if not self.isActive():
            raise UserIsInactiveException(self)
        if self.isOnline():
            raise UserIsOfflineException(self)

        self.setOnline(False)
        self.synchronizeDB()

    def changeSecret(self, secret: str) -> None:
        self.setSecret(secret)
        self.synchronizeDB()

    def changeProfileImage(self, imageID: int) -> None:
        self.setProfileImageID(imageID)
        self.synchronizeDB()

    def changeRole(self, role: str) -> None:
        if role != 'staff' or role != 'customer':
            raise UserRoleDoesNotExistException(role)

        if role == 'staff':
            self.setRole(True)
        else:
            self.setRole(False)

    """ deactivate()
        @pre isActive() == True
    """
    def deactivate(self) -> None:
        if not self.isActive():
            raise UserIsInactiveException(self)
        self.setActive(False)

    """ activate()
        @pre isActive() == False
    """
    def activate(self) -> None:
        if self.isActive():
            raise UserIsActiveException(self)

        self.setActive(True)

    """ updateLastLogin()
        @pre isOnline == True
    """
    def updateLastLogin(self, lastLogin: datetime.datetime) -> None:
        if self.isOnline():
            raise UserIsOnlineException(self)

        self.setLastLogin(lastLogin)
        self.synchronizeDB()

    def verify(self, token: str) -> None:
        if self.isVerified():
            raise UserIsVerifiedException

        if self.getVerificationToken() != token:
            raise UserVerificationFailedException

        self.setVerified(True)

    # helpers and checkers
    def isActive(self) -> bool:
        return self._user.is_active

    def isVerified(self) -> bool:
        return self._user.is_verified

    def isOnline(self) -> bool:
        return self._user.Profile.online

    def isStaff(self) -> bool:
        return self._user.is_staff

    def getNoOfReports(self) -> int:
        return len(self.getReports())

    def getNoOfChats(self) -> int:
        return len(self.getChatIDs())

    def getNoOfSubscriptions(self) -> int:
        return len(self.getSubscriptionIDs())

    def synchronizeDB(self) -> None:
        from UserManagement.Boundaries.DAOs.UserDAO import UserDAO

        dao: UserDAO = UserDAO()
        dao.update(self)

    def hasUserPrivilege(self, action) -> bool:
        for group in self.getGroups():
            if group.hasUserPrivilege(action):
                return True

    def hasReportPrivilege(self, action) -> bool:
        for group in self.getGroups():
            if group.hasReportPrivilege(action):
                return True

    def hasStorePrivilege(self, action) -> bool:
        for group in self.getGroups():
            if group.hasStorePrivilege(action):
                return True

    def hasCategoryPrivilege(self, action) -> bool:
        for group in self.getGroups():
            if group.hasCategoryPrivilege(action):
                return True

    def hasProductPrivilege(self, action) -> bool:
        for group in self.getGroups():
            if group.hasProductPrivilege(action):
                return True

    def hasBarterPrivilege(self, action) -> bool:
        for group in self.getGroups():
            if group.hasBarterPrivilege(action):
                return True

    def hasOfferPrivilege(self, action) -> bool:
        for group in self.getGroups():
            if group.hasOfferPrivilege(action):
                return True

    def hasProofPrivilege(self, action) -> bool:
        for group in self.getGroups():
            if group.hasProofPrivilege(action):
                return True

    def hasNotificationPrivilege(self, action) -> bool:
        for group in self.getGroups():
            if group.hasNotificationPrivilege(action):
                return True

    def hasLogPrivilege(self, action) -> bool:
        for group in self.getGroups():
            if group.hasLogPrivilege(action):
                return True

    def hasFilePrivilege(self, action) -> bool:
        for group in self.getGroups():
            if group.hasFilePrivilege(action):
                return True

    def hasArchivePrivilege(self, action) -> bool:
        for group in self.getGroups():
            if group.hasArchivePrivilege(action):
                return True

    def hasChatPrivilege(self, action) -> bool:
        for group in self.getGroups():
            if group.hasChatPrivilege(action):
                return True

    def hasMembershipPrivilege(self, action) -> bool:
        for group in self.getGroups():
            if group.hasMembershipPrivilege(action):
                return True

    def hasMessagePrivilege(self, action) -> bool:
        for group in self.getGroups():
            if group.hasMessagePrivilege(action):
                return True

    def hasGroupPrivilege(self, action) -> bool:
        for group in self.getGroups():
            if group.hasGroupPrivilege(action):
                return True

    # getters and setter
    def getID(self) -> int:
        return self._user.pk

    def setID(self, userID: int) -> None:
        self._user.pk = userID

    def getFirstName(self) -> str:
        return self._user.first_name

    def setFirstName(self, firstName: str) -> None:
        self._user.first_name = firstName

    def getLastName(self) -> str:
        return self._user.last_name

    def setLastName(self, lastName: str) -> None:
        self._user.last_name = lastName

    def getEmail(self) -> str:
        return self._user.email

    def setEmail(self, email) -> None:
        self._user.email = email

    def getOnline(self) -> bool:
        return self._user.Profile.online

    def setOnline(self, online: bool) -> None:
        self._user.Profile.online = online

    def getRole(self) -> bool:
        if self._user.is_staff:
            return 'staff'
        else:
            return 'customer'

    def setRole(self, role: bool) -> None:
        self._user.is_staff = role

    def getSecret(self) -> str:
        return self._user.password

    def setSecret(self, secret: str) -> None:
        self._user.set_password(secret)

    def getActive(self) -> bool:
        return self._user.is_active

    def setActive(self, active) -> None:
        self._user.is_active = active

    def getDate(self) -> datetime.datetime:
        return self._user.date_joined

    def setDate(self, date: datetime.datetime) -> None:
        self._user.date_joined = date

    def getStoreID(self) -> int:
        return self._user.Profile.storeID

    def setStoreID(self, storeID: int) -> None:
        self._user.Profile.storeID = storeID

    def getReports(self) -> []:
        return self._reports

    def setReports(self, reports: []) -> None:
        self._reports = reports

    def getProfileImageID(self) -> int:
        return self._user.Profile.profileImageID

    def setProfileImageID(self, imageID: int) -> None:
        self._user.Profile.profileImageID = imageID

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
        self._user.last_login = lastLogin

    def getUser(self) -> User:
        return self._user

    def setUser(self, user: User) -> None:
        self._user = user

    def getVerified(self) -> bool:
        return self._user.Profile.verified

    def setVerified(self, verified: str) -> None:
        self._user.Profile.verified = verified

    def getVerificationToken(self) -> str:
        return self._user.Profile.verificationToken

    def setVerificationToken(self, token: str) -> None:
        self._user.Profile.verificationToken = token

