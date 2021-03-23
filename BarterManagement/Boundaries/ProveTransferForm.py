from BarterManagement.Interactors.ProveTransferControl import ProveTransferControl
from FileManagement.Boundaries.FileDTO import FileDTO


class ProveTransferForm:
    """ invariants:
    """

    _control: ProveTransferControl = None
    _fileDTO: FileDTO = None
    _offerID: int = None
    _valid: bool = False
    _submitted: bool = False

    def __init__(self, request):
        offerID = request.POST['offerID']
        filename = request.File['filename']
        #  size, tmpName, extension in a fileDT)
        assert isinstance(offerID, int), "Invalid parameter"
        assert isinstance(filename, str), "Invalid parameter"

        self._valid = True
        self._offerID = offerID

    """ submit()
        @pre isValid() = True
        @pre isSubmitted() = False
        @post isSubmitted() = True
    """
    def submit(self):
        assert self.isValid(), "Invalid request"
        assert not self.isSubmitted(), "Form has already been submitted"

        try:
            control: ProveTransferControl = ProveTransferControl(self._offerID, self._fileDTO)
            control.execute()
        except RuntimeError as exc:
            return exc.args

    def isValid(self):
        return self._valid

    def isSubmitted(self) -> bool:
        return self._submitted
