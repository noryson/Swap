from BarterManagement.Interactors.PlaceOfferControl import PlaceOfferControl


class PlaceOfferForm:
    """ invariants:
    """

    _control: PlaceOfferControl = None
    _barterID: int = None
    _buyerID: int = None
    _offeredItem: str = None
    _valid: bool = False
    _submitted: bool = False

    def __init__(self, request):
        barterID = request.POST['barterID']
        offeredItem = request.POST['offeredItem']
        assert isinstance(barterID, int), "Invalid parameter"
        assert isinstance(offeredItem, str), "Invalid parameter"

        self._valid = True
        self._offeredItem = offeredItem
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
            control: PlaceOfferControl = PlaceOfferControl(self._barterID, self._offeredItem)
            control.execute()
        except RuntimeError as exc:
            return exc.args

    def isValid(self):
        return self._valid

    def isSubmitted(self) -> bool:
        return self._submitted