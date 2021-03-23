class UserExceptions(BaseException):
    pass


class UserIsActiveException(UserExceptions):
    pass


class UserIsInactiveException(UserExceptions):
    pass


class UserIsOnlineException(UserExceptions):
    pass


class UserIsOfflineException(UserExceptions):
    pass


class UserRoleDoesNotExistException(UserExceptions):
    pass


class UserNotFoundException(UserExceptions):
    pass


class UserIsVerifiedException(UserExceptions):
    pass


class UserVerificationFailedException(UserExceptions):
    pass


class UserUpdateFailureException(UserExceptions):
    pass


class UserDeleteFailureException(UserExceptions):
    pass
