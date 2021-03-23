from BarterManagement.Interactors.TerminateBarterControl import TerminateBarterControl


class TerminateBarterButton:
    """ invariants:
        @inv control != None
        @inv barterID != None
    """
    _control: TerminateBarterControl = None
    _barterID: int = None
    _submitted: bool = False

    """ init() takes request, validates it and populate attributes
    """
    def __init__(self, request) -> None:
        barterID = request.POST['barterID']
        assert isinstance(barterID, int), "Invalid Parameter"

        self._valid = True
        self._barterID = barterID

    """ submit() takes the attributes and sends to the interactor
        @pre submitted() = False
        @post submitted() = True
    """
    def submit(self):
        assert self.isValid(), "Invalid request"
        assert not self.isSubmitted(), "Form has already been submitted"

        try:
            self._control = TerminateBarterControl(self._barterID)
            self._control.execute()
            self._control.notifyInterestGroup()
        except RuntimeError as exc:
            return exc.args

        self._submitted = True

    def isValid(self):
        return self._valid

    def isSubmitted(self) -> bool:
        return self._submitted
