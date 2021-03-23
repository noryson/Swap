class GroupException(BaseException):
    pass


class GroupNotFoundException(GroupException):
    pass


class GroupAlreadyExistException(GroupException):
    pass


class GroupContainsUserException(GroupException):
    pass


class GroupDoesNotContainUserException(GroupException):
    pass


class GroupAlreadyHasPrivilegeException(GroupException):
    pass


class GroupDoesNotHavePrivilegeException(GroupException):
    pass