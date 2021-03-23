class FileException(BaseException):
    pass


class FileTooLargeException(FileException):
    pass


class FileExtensionException(FileException):
    pass


class FileTypeException(FileException):
    pass


class FileUploadException(FileException):
    pass