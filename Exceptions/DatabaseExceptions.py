class DBException(BaseException):
    pass

class DBEntryNotFoundException(DBException):
    pass


class DBUpdateFailException(DBException):
    pass


class DBEntryDeletionFailException(DBException):
    pass


class DBEntryCreationFailException(DBException):
    pass