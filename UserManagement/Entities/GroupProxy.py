from UserManagement.Entities.DjangoGroup import DjangoGroup as Group
from UserManagement.Entities.GroupAccess import GroupAccess
import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from UserManagement.Entities.DjangoUser import DjangoUser as User
    from UserManagement.Entities.DjangoPrivilege import DjangoPrivilege


class GroupProxy:

    _realGroupID: int = None
    _realGroup: Group = None
    _access: GroupAccess = None

    def proxyCheck(self) -> None:
        if self._realGroup is None:
            from UserManagement.Boundaries.DAOs.GroupDAO import GroupDAO
            GroupDao = GroupDAO()
            self._realGroup = GroupDao.get(self._realGroupID)
            self._access = GroupAccess(self._realGroup)

    def getRealGroupID(self) -> int:
        return self._realGroupID

    def setRealGroupID(self, newID: int) -> None:
        self._realGroupID = newID


    def addUser(self, user: User) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('addUser'):
            raise PermissionError(self._access)
        else:
            self._realGroup.addUser(user)

    def removeUser(self, user: User) -> None:
        self.proxyCheck()
        if not self._access.isAccessible('addUser'):
            raise PermissionError(self._access)
        else:
            self._realGroup.removeUser(user)

    # helpers and checkers

    # def canCreateUser(self) -> bool:
    #     return self._UserPrivilege.canCreate()
    #     return self._privilege.hasPrivilege('user', 'create')

    def hasUserPrivilege(self, action: str) -> bool:
        self.proxyCheck()
        return self._realGroup.hasUserPrivilege(action)

    def hasReportPrivilege(self, action: str) -> bool:
        self.proxyCheck()
        return self._realGroup.hasReportPrivilege(action)

    def hasStorePrivilege(self, action: str) -> bool:
        self.proxyCheck()
        return self._realGroup.hasStorePrivilege(action)

    def hasCategoryPrivilege(self, action: str) -> bool:
        self.proxyCheck()
        return self._realGroup.hasCategoryPrivilege(action)

    def hasProductPrivilege(self, action: str) -> bool:
        self.proxyCheck()
        return self._realGroup.hasProductPrivilege(action)

    def hasBarterPrivilege(self, action: str) -> bool:
        self.proxyCheck()
        return self._realGroup.hasBarterPrivilege(action)

    def hasOfferPrivilege(self, action: str) -> bool:
        self.proxyCheck()
        return self._realGroup.hasOfferPrivilege(action)

    def hasProofPrivilege(self, action: str) -> bool:
        self.proxyCheck()
        return self._realGroup.hasProofPrivilege(action)

    def hasNotificationPrivilege(self, action: str) -> bool:
        self.proxyCheck()
        return self._realGroup.hasNotificationPrivilege(action)

    def hasLogPrivilege(self, action: str) -> bool:
        self.proxyCheck()
        return self._realGroup.hasLogPrivilege(action)

    def hasFilePrivilege(self, action: str) -> bool:
        self.proxyCheck()
        return self._realGroup.hasFilePrivilege(action)

    def hasArchivePrivilege(self, action: str) -> bool:
        self.proxyCheck()
        return self._realGroup.hasArchivePrivilege(action)

    def hasChatPrivilege(self, action: str) -> bool:
        self.proxyCheck()
        return self._realGroup.hasChatPrivilege(action)

    def hasMembershipPrivilege(self, action: str) -> bool:
        self.proxyCheck()
        return self._realGroup.hasMembershipPrivilege(action)

    def hasMessagePrivilege(self, action: str) -> bool:
        self.proxyCheck()
        return self._realGroup.hasMessagePrivilege(action)

    def hasGroupPrivilege(self, action: str) -> bool:
        self.proxyCheck()
        return self._realGroup.hasGroupPrivilege(action)


    # getters and setters
    def getID(self) -> int:
        self.proxyCheck()
        return self._realGroup.getID()

    def setID(self, groupID: int) -> None:
        self.proxyCheck()
        self._realGroup.setID(groupID)

    def getName(self) -> str:
        self.proxyCheck()
        return self._realGroup.getName()

    def setName(self, name) -> None:
        self.proxyCheck()
        self._realGroup.setName(name)

    def getDate(self) -> datetime.datetime:
        self.proxyCheck()
        return self._realGroup.getDate()

    def setDate(self, date: datetime.datetime) -> None:
        self.proxyCheck()
        self._realGroup.setDate(date)

    def getPrivilege(self) -> DjangoPrivilege:
        self.proxyCheck()
        return self._realGroup.getPrivilege()

    def setPrivilege(self, privilege: DjangoPrivilege) -> None:
        self.proxyCheck()
        self._realGroup.setPrivilege(privilege)

    def getUsers(self) -> []:
        self.proxyCheck()
        return self._realGroup.getUsers()

    def setUsers(self, users: []) -> None:
        self.proxyCheck()
        self._realGroup.setUsers(users)
