from django.contrib.auth.models import User
from UserManagement.Entities.Privilege import Privilege as SwapPrivilege
from UserManagement.Entities.DjangoGroup import DjangoGroup
from django.contrib.auth.models import Group


class DjangoPrivilege(SwapPrivilege):
    _group: DjangoGroup = None

    """" givePrivilege()
    """
    def givePrivilege(self, entity: str, action: str) -> None:
        group = self._group.getGroup()

        if action == 'create':
            action = 'can add '+entity
        elif action == 'read':
            action = 'can view '+entity
        elif action == 'update':
            action = 'can change '+entity
        elif action == 'delete':
            action = 'can delete '+entity

        group.permissions.add(action)
        self.synchronizeDB()

    def removePrivilege(self, entity: str, action: str) -> None:
        group = self._group.getGroup()

        if action == 'create':
            action = 'can add ' + entity
        elif action == 'read':
            action = 'can view ' + entity
        elif action == 'update':
            action = 'can change ' + entity
        elif action == 'delete':
            action = 'can delete ' + entity

        group.permissions.remove(action)
        self.synchronizeDB()

    # helpers and checkers
    def hasPrivilege(self, entity: str, action: str) -> bool:
        group = self._group.getGroup()

        if action == 'create':
            action = 'add'
        elif action == 'read':
            action = 'view'
        elif action == 'update':
            action = 'change'

        action = 'can '+action+' '+entity

        try:
            group.permissions.get(name=action)
            return True
        except:
            return False

    def synchronizeDB(self) -> None:
        group = self._group.getGroup()
        group.save()

    # getters and setters
    def getGroup(self) -> DjangoGroup:
        return self._group

    def setGroup(self, group: DjangoGroup) -> None:
        self._group = group

    def getPrivileges(self) -> {}:
        pass

    def setPrivileges(self, privileges: {}) -> None:
        pass
