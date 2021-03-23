from BarterManagement.Interactors.HostBarterControl import HostBarterControl
import datetime


class HostBarterForm:
    _hostBarterControl: HostBarterControl = None
    _productID: int = None
    _requestedItem: str = None
    _endDate: datetime.datetime = None
    _valid: bool = False
    _submitted: bool = False

    """ cleans input and initializes attributes
    """
    def __init__(self, request) -> None:
        productID = request.POST['productID']
        requestedItem = request.POST['requestedItem']
        endDate = request.POST['endDate']

        assert isinstance(productID, int), "Invalid product ID"
        assert isinstance(requestedItem, str), "Invalid request item"
        assert isinstance(endDate, datetime.datetime), "Invalid date"

        self._valid = True
        self._productID = productID
        self._requestedItem = requestedItem
        self._endDate = endDate

    """ submit()
        @pre isValid() = True
        @pre isSubmitted() = False
        @post isSubmitted() = True
    """
    def submit(self):
        assert self.isValid(), "Invalid request"
        assert not self.isSubmitted(), "Form has already been submitted"

        try:
            self._hostBarterControl = HostBarterControl(self._productID, self._endDate, self._requestedItem)
            self._hostBarterControl.execute()
            self._hostBarterControl.notifySubscribers()
        except RuntimeError as exc:
            return exc.args

        self._submitted = True

    def isValid(self):
        return self._valid

    def isSubmitted(self) -> bool:
        return self._submitted


