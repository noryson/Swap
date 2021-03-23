from FileManagement.Boundaries.FileDTO import FileDTO
from Exceptions.FileExceptions import *

class ProofUploader:
    _fileID: int = None

    def __init__(self, fileDTO: FileDTO) -> None:
        pass

    def upload(self) -> None:
        pass

    def getFileID(self) -> int:
        return self._fileID

class Uploader:
    def upload(self, file: fileDTO):
        pass