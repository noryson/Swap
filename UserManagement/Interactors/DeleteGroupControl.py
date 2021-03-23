from UserManagement.Entities.GroupProxy import GroupProxy
from UserManagement.Entities.GroupAccess import GroupAccess
from Exceptions.GroupExceptions import *


class DeleteGroupControl:
    _group: GroupProxy = None

    def __init__(self, groupID: int) -> None:
        try:
            group: GroupProxy = GroupProxy()
            group.setID(groupID)
            group.proxyCheck()
        except GroupNotFoundException:
            raise RuntimeError(groupID)

        self._group = group

    def execute(self) -> None:
        try:
            from UserManagement.Boundaries.DAOs.GroupDAO import GroupDAO
            group: GroupProxy = self.getGroup()
            access: GroupAccess = GroupAccess(group._realGroup)
            if not access.isAccessible('delete'):
                raise PermissionError(access)
            groupDao: GroupDAO = GroupDAO()
            groupDao.delete(self.getGroup().getID())
        except PermissionError:
            raise RuntimeError('Access denied.')

