from UserManagement.Entities.GroupProxy import GroupProxy
from UserManagement.Entities.GroupAccess import GroupAccess
from Exceptions.GroupExceptions import *


class DisplayGroupControl:
    _group: GroupProxy = None

    def __init__(self, groupID: int) -> None:
        try:
            group: GroupProxy = GroupProxy()
            group.setID(groupID)
            group.proxyCheck()
        except GroupNotFoundException:
            raise RuntimeError(groupID)

        self._group = group

    def execute(self):
        try:
            from UserManagement.Boundaries.DAOs.GroupDAO import GroupDAO
            group: GroupProxy = self.getGroup()
            access: GroupAccess = GroupAccess(group._realGroup)
            if not access.isAccessible('display'):
                raise PermissionError(access)
        except PermissionError:
            raise RuntimeError('Access denied.')

        return group

