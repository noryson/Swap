class CategoryException(BaseException):
    pass


class CategoryCreationFailureException(CategoryException):
    pass


class CategoryNotFoundException(CategoryException):
    pass


class CategoryUpdateFailureException(CategoryException):
    pass


class CategoryDeleteFailureException(CategoryException):
    pass


class CategoryNameExistException(CategoryException):
    pass