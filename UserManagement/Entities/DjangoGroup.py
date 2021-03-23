from UserManagement.Entities.Group import Group as SwapGroup
from UserManagement.Entities.DjangoUser import DjangoUser
from UserManagement.Entities.DjangoPrivilege import DjangoPrivilege
import datetime
from django.contrib.auth.models import Group


class DjangoGroup(SwapGroup):
    _ID: int = None
    _name: str = None
    _users: [DjangoUser] = None
    # _privilege: DjangoPrivilege = None
    _privilege = None
    _dateCreated: datetime.datetime = None

    _group: Group = None

    """ addUser(user)
        @pre Users !contain user
    """
    def addUser(self, user: DjangoUser) -> None:
        self._group.add(user.getUser())  # fixme add to django group

    def removeUser(self, user: DjangoUser) -> None:
        pass

    # helpers and checkers

    # def canCreateUser(self) -> bool:
    #     return self._UserPrivilege.canCreate()
    #     return self._privilege.hasPrivilege('user', 'create')

    def hasUserPrivilege(self, action: str) -> bool:
        if action == 'create':
            action = 'add'
        elif action == 'read':
            action = 'view'
        elif action == 'update':
            action = 'change'

        try:
            self._group.permissions.get(name='Can '+action+' user')
            return True
        except:
            return False

    def hasReportPrivilege(self, action: str) -> bool:
        if action == 'create':
            action = 'add'
        elif action == 'read':
            action = 'view'
        elif action == 'update':
            action = 'change'

        try:
            self._group.permissions.get(name='Can '+action+' report')
            return True
        except:
            return False

    def hasStorePrivilege(self, action: str) -> bool:
        if action == 'create':
            action = 'add'
        elif action == 'read':
            action = 'view'
        elif action == 'update':
            action = 'change'

        try:
            self._group.permissions.get(name='Can '+action+' store')
            return True
        except:
            return False

    def hasCategoryPrivilege(self, action: str) -> bool:
        if action == 'create':
            action = 'add'
        elif action == 'read':
            action = 'view'
        elif action == 'update':
            action = 'change'

        try:
            self._group.permissions.get(name='Can '+action+' category')
            return True
        except:
            return False

    def hasProductPrivilege(self, action: str) -> bool:
        if action == 'create':
            action = 'add'
        elif action == 'read':
            action = 'view'
        elif action == 'update':
            action = 'change'

        try:
            self._group.permissions.get(name='Can '+action+' product')
            return True
        except:
            return False

    def hasBarterPrivilege(self, action: str) -> bool:
        if action == 'create':
            action = 'add'
        elif action == 'read':
            action = 'view'
        elif action == 'update':
            action = 'change'

        try:
            self._group.permissions.get(name='Can '+action+' barter')
            return True
        except:
            return False

    def hasOfferPrivilege(self, action: str) -> bool:
        if action == 'create':
            action = 'add'
        elif action == 'read':
            action = 'view'
        elif action == 'update':
            action = 'change'

        try:
            self._group.permissions.get(name='Can '+action+' offer')
            return True
        except:
            return False

    def hasProofPrivilege(self, action: str) -> bool:
        if action == 'create':
            action = 'add'
        elif action == 'read':
            action = 'view'
        elif action == 'update':
            action = 'change'

        try:
            self._group.permissions.get(name='Can '+action+' proof')
            return True
        except:
            return False

    def hasNotificationPrivilege(self, action: str) -> bool:
        if action == 'create':
            action = 'add'
        elif action == 'read':
            action = 'view'
        elif action == 'update':
            action = 'change'

        try:
            self._group.permissions.get(name='Can '+action+' notification')
            return True
        except:
            return False

    def hasLogPrivilege(self, action: str) -> bool:
        if action == 'create':
            action = 'add'
        elif action == 'read':
            action = 'view'
        elif action == 'update':
            action = 'change'

        try:
            self._group.permissions.get(name='Can '+action+' log')
            return True
        except:
            return False

    def hasFilePrivilege(self, action: str) -> bool:
        if action == 'create':
            action = 'add'
        elif action == 'read':
            action = 'view'
        elif action == 'update':
            action = 'change'

        try:
            self._group.permissions.get(name='Can '+action+' file')
            return True
        except:
            return False

    def hasArchivePrivilege(self, action: str) -> bool:
        if action == 'create':
            action = 'add'
        elif action == 'read':
            action = 'view'
        elif action == 'update':
            action = 'change'

        try:
            self._group.permissions.get(name='Can '+action+' archive')
            return True
        except:
            return False

    def hasChatPrivilege(self, action: str) -> bool:
        if action == 'create':
            action = 'add'
        elif action == 'read':
            action = 'view'
        elif action == 'update':
            action = 'change'

        try:
            self._group.permissions.get(name='Can '+action+' chat')
            return True
        except:
            return False

    def hasMembershipPrivilege(self, action: str) -> bool:
        if action == 'create':
            action = 'add'
        elif action == 'read':
            action = 'view'
        elif action == 'update':
            action = 'change'

        try:
            self._group.permissions.get(name='Can '+action+' membership')
            return True
        except:
            return False

    def hasMessagePrivilege(self, action: str) -> bool:
        if action == 'create':
            action = 'add'
        elif action == 'read':
            action = 'view'
        elif action == 'update':
            action = 'change'

        try:
            self._group.permissions.get(name='Can '+action+' message')
            return True
        except:
            return False

    def hasGroupPrivilege(self, action: str) -> bool:
        if action == 'create':
            action = 'add'
        elif action == 'read':
            action = 'view'
        elif action == 'update':
            action = 'change'

        try:
            self._group.permissions.get(name='Can '+action+' group')
            return True
        except:
            return False


    def synchronizeDB(self) -> None:
        self._group.save()

    # getters and setters
    def getID(self) -> int:
        return self._ID

    def setID(self, groupID: int) -> None:
        self._ID = groupID

    def getName(self) -> str:
        return self._name

    def setName(self, name) -> None:
        self._name = name

    def getDate(self) -> datetime.datetime:
        return self._dateCreated

    def setDate(self, date: datetime.datetime) -> None:
        self._dateCreated = date

    def getPrivilege(self) -> DjangoPrivilege:
        return self._privilege

    def setPrivilege(self, privilege: DjangoPrivilege) -> None:
        self._privilege = privilege

    def getUsers(self) -> []:
        return self._users

    def setUsers(self, user: []) -> None:
        self._users = user

    def getGroup(self) -> Group:
        return self._group

    def setGroup(self, group: Group) -> None:
        self._group = group


