from BarterManagement.Interactors.GetBarterControl import GetBarterControl
from BarterManagement.Boundaries.DTO import BarterDTO


class GetBarterForm:
    """ invariants:
        @inv barterID != None
    """

    _control: GetBarterControl = None
    _barterID: int = None
    _valid: bool = False
    _submitted: bool = False

    def __init__(self, request):
        barterID = request.POST['barterID']
        assert isinstance(barterID, int), "Invalid Parameter"

        self._valid = True
        self._barterID = barterID

    """ submit()
        @pre isValid() = True
        @pre isSubmitted() = False
        @post isSubmitted() = True
    """
    def submit(self):
        assert self.isValid(), "Invalid request"
        assert not self.isSubmitted(), "Form has already been submitted"

        try:
            self._control = GetBarterControl(self._barterID)
            dto: BarterDTO = self._control.execute()
            self._submitted = True
            return dto
        except RuntimeError as exc:
            return exc.args

    def isValid(self) -> bool:
        return self._valid

    def isSubmitted(self) -> bool:
        return self._submitted