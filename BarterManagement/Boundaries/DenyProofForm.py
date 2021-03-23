from BarterManagement.Interactors.DenyProofControl import DenyProofControl


class DenyProofForm:
    """ invariants:
        @inv no None values
    """

    _control: DenyProofControl = None
    _proofID: int = None
    _valid: bool = False
    _submitted: bool = False

    def __init__(self, request):
        proofID = request.POST['proofID']
        assert isinstance(proofID, int), 'Invalid parameter'

        self._valid = True
        self._proofID = proofID

    """ submit()
        @pre isValid() = True
        @pre isSubmitted() = False
        @post isSubmitted() = True
    """
    def submit(self):
        assert self.isValid(), "Invalid request"
        assert not self.isSubmitted(), "Form has already been submitted"

        try:
            control: DenyProofControl = DenyProofControl(self._proofID)
            control.execute()
        except RuntimeError as exc:
            return exc.args

    def isValid(self):
        return self._valid

    def isSubmitted(self) -> bool:
        return self._submitted
