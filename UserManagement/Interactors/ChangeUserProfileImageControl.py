from UserManagement.Entities.UserProxy import UserProxy
from Exceptions.UserExceptions import *


class ChangeUserProfileImageControl:
    _user: UserProxy = None
    _imageID: int = None

    def __init__(self, userID: int, imageID: int) -> None:
        try:
            user: UserProxy = UserProxy()
            user.setID(userID)
            user.proxyCheck
        except UserNotFoundException:
            raise RuntimeError(userID)

        self._user = user
        self._imageID = imageID
        # self.setUser(user)

    def execute(self) -> None:
        try:
            self._user.changeProfileImage(self._imageID)
        except PermissionError:
            raise RuntimeError('Access denied')

