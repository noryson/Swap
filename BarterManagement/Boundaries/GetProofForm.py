from BarterManagement.Interactors.GetProofControl import GetProofControl
from BarterManagement.Boundaries.DTO import ProofDTO

class GetProofForm:
    """ invariants:
        @inv proofID != None
    """

    _control: GetProofControl = None
    _proofID: int = None
    _valid: bool = None
    _submitted: bool = None

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
            control = GetProofControl(self._proofID)
            # dto: ProofDTO = control.execute()
            dto = control.execute()
            self._submitted = True
            return dto
        except RuntimeError as exc:
            return exc.args

    def isValid(self) -> bool:
        return self._valid

    def isSubmitted(self) -> bool:
        return self._submitted
