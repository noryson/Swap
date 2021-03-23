from StoreManagement.Interactors.SubscribeToStoreControl import SubscribeToStoreControl


class SubscribeToStoreForm:
    """ invariants:
    """

    _control: SubscribeToStoreControl = None
    _storeID: int = None
    _valid: bool = False
    _submitted: bool = False

    def __init__(self, request) -> None:
        storeID = request.POST['storeID']
        assert isinstance(storeID, int), "Invalid parameter"

        self._storeID = storeID
        self._valid = True

    def submit(self):
        assert self.isValid(), "Invalid request"
        assert not self.isSubmitted(), "Form has already been submitted"

        self._submitted = True
        try:
            control = SubscribeToStoreControl(self._storeID)
            control.execute()
        except RuntimeError as exc:
            print(exc.args)
            return exc.args

    def isValid(self) -> bool:
        return self._valid

    def isSubmitted(self) -> bool:
        return self._submitted
