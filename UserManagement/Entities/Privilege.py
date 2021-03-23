from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from UserManagement.Entities.User import User
from UserManagement.Entities.Group import Group


class Privilege:
    _group: Group = None
    _privileges: {} = dict(user=dict(create=False, read=False, update=False, delete=False),
                           privilege=dict(create=False, read=False, update=False, delete=False),
                           report=dict(create=False, read=False, update=False, delete=False),
                           store=dict(create=False, read=False, update=False, delete=False),
                           category=dict(create=False, read=False, update=False, delete=False),
                           product=dict(create=False, read=False, update=False, delete=False),
                           barter=dict(create=False, read=False, update=False, delete=False),
                           offer=dict(create=False, read=False, update=False, delete=False),
                           proof=dict(create=False, read=False, update=False, delete=False),
                           notification=dict(create=False, read=False, update=False, delete=False),
                           log=dict(create=False, read=False, update=False, delete=False),
                           file=dict(create=False, read=False, update=False, delete=False),
                           archive=dict(create=False, read=False, update=False, delete=False),
                           chat=dict(create=False, read=False, update=False, delete=False),
                           membership=dict(create=False, read=False, update=False, delete=False),
                           message=dict(create=False, read=False, update=False, delete=False),
                           group=dict(create=False, read=False, update=False, delete=False),
                           )

    def givePrivilege(self, entity: str, action: str) -> None:
        self._privileges[entity][action] = True

    def removePrivilege(self, entity: str, action: str) -> None:
        self._privileges[entity][action] = False

    # helpers and checkers
    def hasPrivilege(self, entity: str, action: str) -> bool:
        return self._privileges[entity][action]

    # getters and setters
    def getPrivileges(self) -> {}:
        return self._privileges

    def setPrivileges(self, privileges: {}) -> None:
        self._privileges = privileges
