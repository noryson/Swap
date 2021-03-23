from BarterManagement.Interactors.DeclineOfferControl import DeclineOfferControl


class DeclineOfferButton:
    """ invariants:
    """

    _control: DeclineOfferControl = None
    _offerID: int = None
    _valid: bool = False
    _submitted: bool = False

    def __init__(self, request):
        offerID = request.POST['offerID']
        assert isinstance(offerID, int), "Invalid parameter"

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
            control: DeclineOfferControl = DeclineOfferControl(self._offerID)
            control.execute()
        except RuntimeError as exc:
            return exc.args

    def isValid(self):
        return self._valid

    def isSubmitted(self) -> bool:
        return self._submitted