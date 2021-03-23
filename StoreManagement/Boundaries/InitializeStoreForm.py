from StoreManagement.Interactors.InitializeStoreControl import InitializeStoreControl


class InitializeStoreForm:
    """ invariants:
    """

    _control: InitializeStoreControl = None
    _ownerID: int = None
    _maxNoOfProducts: int = None
    _valid: bool = False
    _submitted: bool = False

    def __init__(self, request) -> None:
        ownerID = request.POST['ownerID']
        maxNoOfProducts = request.POST['maxNoOfProducts']
        assert isinstance(ownerID, int), "Invalid parameter"
        assert isinstance(maxNoOfProducts, int), "Invalid parameter"

        self._valid = True
        self._ownerID = ownerID
        self._maxNoOfProducts = maxNoOfProducts

    def submit(self) -> None:
        assert self.isValid(), "Invalid request"
        assert not self.isSubmitted(), "Form has already been submitted"

        self._submitted = True
        try:
            control = InitializeStoreControl(self._ownerID, self._maxNoOfProducts)
            control.execute()
        except RuntimeError as exc:
            print(exc.args)
            return exc.args

    def isValid(self) -> bool:
        return self._valid

    def isSubmitted(self) -> bool:
        return self._submitted
