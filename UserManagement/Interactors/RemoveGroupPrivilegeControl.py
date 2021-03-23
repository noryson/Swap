from UserManagement.Interactors.DisplayPrivilegeControl import DisplayPrivilegeControl
from UserManagement.Entities.GroupProxy import GroupProxy
from UserManagement.Entities.GroupAccess import GroupAccess
from Exceptions.GroupExceptions import *
from Exceptions.PrivilegeExceptions import *


class RemoveGroupPrivilegeControl:
    _group: GroupProxy = None
    _entity: str = None
    _action: str = None

    def __init__(self, groupID: int, entity: str, action: str) -> None:
        try:
            group: GroupProxy = GroupProxy()
            group.setID(groupID)
            group.proxyCheck()

            privileges: [] = DisplayPrivilegeControl()
            for prvlg in privileges:
                try:
                    e = prvlg[entity][action]
                except KeyError:
                    raise PrivilegeNotFoundException(entity, action)
        except GroupNotFoundException:
            raise RuntimeError('group does not exist')
        except PrivilegeNotFoundException:
            raise RuntimeError('privilege does not exist')

        self._entity = entity
        self._action = action

    def execute(self) -> None:
        try:
            self._group.getPrivilege().removePrivilege(self._entity, self._action)
        except GroupDoesNotHavePrivilegeException:
            raise RuntimeError('Group does have this privilege')
        except PermissionError:
            raise RuntimeError('Access denied.')

