from UserManagement.Entities.DjangoUser import DjangoUser as User
from UserManagement.Entities.UserAccess import UserAccess
import datetime


class UserProxy:

    _realUserID: int = None
    _realUser: User = None
    _access: UserAccess = None

    def proxyCheck(self) -> None:
        if self._realUser is None:
            from UserManagement.Boundaries.DAOs.UserDAO import UserDAO
            UserDao = UserDAO()
            self._realUser = UserDao.get(self._realUserID)
            self._access = UserAccess(self._realUser)

    def getRealUserID(self) -> int:
        return self._realUserID

    def setRealUserID(self, newID: int) -> None:
        self._realUserID = newID


    def login(self) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('login'):
            raise PermissionError(self._access)
        else:
            self._realUser.login()

    def logout(self) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('logout'):
            raise PermissionError(self._access)
        else:
            self._realUser.logout()

    def changeSecret(self, secret: str) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('changeSecret'):
            raise PermissionError(self._access)
        else:
            self._realUser.changeSecret(secret)

    def changeProfileImage(self, imageID: int) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('changeProfileImage'):
            raise PermissionError(self._access)
        else:
            self._realUser.changeProfileImage(imageID)

    def changeRole(self, role: str) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('login'):
            raise PermissionError(self._access)
        else:
            self._realUser.changeRole(role)

    def deactivate(self) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('deactivate'):
            raise PermissionError(self._access)
        else:
            self._realUser.deactivate()

    def activate(self) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('activate'):
            raise PermissionError(self._access)
        else:
            self._realUser.activate()

    def updateLastLogin(self, lastLogin: datetime.datetime) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('updateLastLogin'):
            raise PermissionError(self._access)
        else:
            self._realUser.updateLastLogin(lastLogin)

    def verify(self, token: str) -> None:
        self.proxyCheck()
        self._realUser.verify(token)

    # helpers and checkers
    def isActive(self) -> bool:
        self.proxyCheck()
        return self._realUser.isActive()

    def isVerified(self) -> bool:
        self.proxyCheck()
        return self._realUser.isVerified()

    def isOnline(self) -> bool:
        self.proxyCheck()
        return self._realUser.isOnline()

    def isStaff(self) -> bool:
        self.proxyCheck()
        return self._realUser.isStaff()

    def getNoOfReports(self) -> int:
        self.proxyCheck()
        return self._realUser.getNoOfReports()

    def getNoOfChats(self) -> int:
        self.proxyCheck()
        return self._realUser.getNoOfChats()

    def getNoOfSubscriptions(self) -> int:
        self.proxyCheck()
        return self._realUser.getNoOfSubscriptions()

    def hasUserPrivilege(self, action) -> bool:
        self.proxyCheck()
        return self._realUser.hasUserPrivilege(action)

    def hasReportPrivilege(self, action) -> bool:
        self.proxyCheck()
        return self._realUser.hasReportPrivilege(action)

    def hasStorePrivilege(self, action) -> bool:
        self.proxyCheck()
        return self._realUser.hasStorePrivilege(action)

    def hasCategoryPrivilege(self, action) -> bool:
        self.proxyCheck()
        return self._realUser.hasCategoryPrivilege(action)

    def hasProductPrivilege(self, action) -> bool:
        self.proxyCheck()
        return self._realUser.hasProductPrivilege(action)

    def hasBarterPrivilege(self, action) -> bool:
        self.proxyCheck()
        return self._realUser.hasBarterPrivilege(action)

    def hasOfferPrivilege(self, action) -> bool:
        self.proxyCheck()
        return self._realUser.hasOfferPrivilege(action)

    def hasProofPrivilege(self, action) -> bool:
        self.proxyCheck()
        return self._realUser.hasProofPrivilege(action)

    def hasNotificationPrivilege(self, action) -> bool:
        self.proxyCheck()
        return self._realUser.hasNotificationPrivilege(action)

    def hasLogPrivilege(self, action) -> bool:
        self.proxyCheck()
        return self._realUser.hasLogPrivilege(action)

    def hasFilePrivilege(self, action) -> bool:
        self.proxyCheck()
        return self._realUser.hasFilePrivilege(action)

    def hasArchivePrivilege(self, action) -> bool:
        self.proxyCheck()
        return self._realUser.hasArchivePrivilege(action)

    def hasChatPrivilege(self, action) -> bool:
        self.proxyCheck()
        return self._realUser.hasChatPrivilege(action)

    def hasMembershipPrivilege(self, action) -> bool:
        self.proxyCheck()
        return self._realUser.hasMembershipPrivilege(action)

    def hasMessagePrivilege(self, action) -> bool:
        self.proxyCheck()
        return self._realUser.hasMessagePrivilege(action)

    def hasGroupPrivilege(self, action) -> bool:
        self.proxyCheck()
        return self._realUser.hasGroupPrivilege(action)

    # getters and setter
    def getID(self) -> int:
        self.proxyCheck()
        return self._realUser.getID()

    def setID(self, userID: int) -> None:
        self.proxyCheck()
        self._realUser.setID(userID)

    def getFirstName(self) -> str:
        self.proxyCheck()
        return self._realUser.getFirstName()

    def setFirstName(self, firstName: str) -> None:
        self.proxyCheck()
        self._realUser.setFirstName(firstName)

    def getLastName(self) -> str:
        self.proxyCheck()
        return self._realUser.getLastName()

    def setLastName(self, lastName: str) -> None:
        self.proxyCheck()
        self._realUser.setLastName(lastName)

    def getEmail(self) -> str:
        self.proxyCheck()
        return self._realUser.getEmail()

    def setEmail(self, email) -> None:
        self.proxyCheck()
        self._realUser.setEmail(email)

    def getOnline(self) -> bool:
        self.proxyCheck()
        return self._realUser.getOnline()

    def setOnline(self, online: bool) -> None:
        self.proxyCheck()
        self._realUser.setOnline(online)

    def getRole(self) -> bool:
        self.proxyCheck()
        return self._realUser.getRole()

    def setRole(self, role: bool) -> None:
        self.proxyCheck()
        self._realUser.setRole(role)

    def getSecret(self) -> str:
        self.proxyCheck()
        return self._realUser.getSecret()

    def setSecret(self, secret: str) -> None:
        self.proxyCheck()
        self._realUser.setSecret(secret)

    def getActive(self) -> bool:
        self.proxyCheck()
        return self._realUser.getActive()

    def setActive(self, active) -> None:
        self.proxyCheck()
        self._realUser.setActive(active)

    def getDate(self) -> datetime.datetime:
        self.proxyCheck()
        return self._realUser.getDate()

    def setDate(self, date: datetime.datetime) -> None:
        self.proxyCheck()
        self._realUser.setDate(date)

    def getStoreID(self) -> int:
        self.proxyCheck()
        return self._realUser.getStoreID()

    def setStoreID(self, storeID: int) -> None:
        self.proxyCheck()
        self._realUser.setStoreID(storeID)

    def getReports(self) -> []:
        self.proxyCheck()
        return self._realUser.getReports()

    def setReports(self, reports: []) -> None:
        self.proxyCheck()
        self._realUser.setReports(reports)

    def getProfileImageID(self) -> int:
        self.proxyCheck()
        return self._realUser.getProfileImageID()

    def setProfileImageID(self, imageID: int) -> None:
        self.proxyCheck()
        self._realUser.setProfileImageID(imageID)

    def getChatIDs(self) -> []:
        self.proxyCheck()
        return self._realUser.getChatIDs()

    def setChatIDs(self, chatIDs: []) -> None:
        self.proxyCheck()
        self._realUser.setChatIDs(chatIDs)

    def getSubscriptionIDs(self) -> []:
        self.proxyCheck()
        return self._realUser.getSubscriptionIDs()

    def setSubscriptionIDs(self, subscriptionIDs: []) -> None:
        self.proxyCheck()
        self._realUser.setSubscriptionIDs(subscriptionIDs)

    def getGroups(self) -> []:
        self.proxyCheck()
        return self._realUser.getGroups()

    def setGroups(self, groups: []) -> None:
        self.proxyCheck()
        self._realUser.setGroups(groups)

    def getLastLogin(self) -> datetime.datetime:
        self.proxyCheck()
        return self._realUser.getLastLogin()

    def setLastLogin(self, lastLogin: datetime.datetime) -> None:
        self.proxyCheck()
        self._realUser.setLastLogin(lastLogin)

    def getVerified(self) -> bool:
        self.proxyCheck()
        return self._realUser.getVerified()

    def setVerified(self, verified: str) -> None:
        self.proxyCheck()
        self._realUser.setVerified(verified)

    def getVerificationToken(self) -> str:
        self.proxyCheck()
        return self._realUser.getVerificationToken()

    def setVerificationToken(self, token: str) -> None:
        self.proxyCheck()
        self._realUser.setVerificationToken(token)

