from UserManagement.Entities.GroupProxy import GroupProxy
from UserManagement.Entities.GroupAccess import GroupAccess
from Exceptions.GroupExceptions import *


class CreateGroupControl:
    _name: str = None

    def __init__(self, name: str) -> None:
        self._name = name
        # self.setUser(user)

    def execute(self) -> None:
        try:
            access: GroupAccess = GroupAccess()
            if not access.isAccessible("create"):
                raise PermissionError
        except PermissionError:
            raise RuntimeError('Access denied')

        from UserManagement.Boundaries.DAOs.GroupDAO import GroupDAO
        dao = GroupDAO()

        try:
            groups = dao.getAll()
            for group in groups:
                if group.getName() == self._name:
                    raise GroupAlreadyExistException(self._name)
        except GroupAlreadyExistException:
            raise RuntimeError('Group already exist')

        dao.create(self._name)


