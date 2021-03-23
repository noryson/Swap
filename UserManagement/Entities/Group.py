from UserManagement.Entities.Privilege import Privilege
import datetime
from UserManagement.Entities.User import User


class Group:
    _ID: int = None
    _name: str = None
    _users: [User] = None
    _privilege: Privilege = None
    _dateCreated: datetime.datetime = None

    def addUser(self, user: User) -> None:
        self._users.append(user)

    def removeUser(self, user: User) -> None:
        pass

    # helpers and checkers
    # def canCreateUser(self) -> bool:
    #     return self._UserPrivilege.canCreate()
    #     return self._privilege.hasPrivilege('user', 'create')

    def synchronizeDB(self) -> None:
        pass

    # getters and setters
    def getID(self) -> int:
        return self._ID

    def setID(self, groupID: int) -> None:
        self._ID = groupID

    def getName(self) -> str:
        return self._name

    def setName(self, name) -> None:
        self._name = name

    def getPrivilege(self) -> Privilege:
        return self._privilege

    def setPrivilege(self, privilege: Privilege) -> None:
        self._privilege = privilege

    def getDate(self) -> datetime.datetime:
        return self._dateCreated

    def setDate(self, date: datetime.datetime) -> None:
        self._dateCreated = date

    def getUsers(self) -> []:
        return self._users

    def setUsers(self, user: []) -> None:
        self._users = user