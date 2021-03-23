from UserManagement.Entities.UserProxy import UserProxy
from Exceptions.UserExceptions import *


class VerifyUserControl:
    _user: UserProxy = None
    _verificationToken: str = None

    def __init__(self, userID: int, verificationToken: str) -> None:
        try:
            user: UserProxy = UserProxy()
            user.setID(userID)
            user.proxyCheck
        except UserNotFoundException:
            raise RuntimeError(userID)

        self._user = user
        self._verificationToken = verificationToken
        # self.setUser(user)

    def execute(self) -> None:
        try:
            self._user.verify(self._verificationToken)
        except UserIsVerifiedException:
            raise RuntimeError('User is active')
        except UserVerificationFailedException:
            raise RuntimeError('Verification failed')
        except PermissionError:
            raise RuntimeError('Access denied')

