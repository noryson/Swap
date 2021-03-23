from BarterManagement.Interactors.FindBarterControl import FindBarterControl
from BarterManagement.Boundaries.DTO import BarterDTO
from Exceptions.BarterExceptions import *


class BarterFinderService:
    """ invariants:
        @inv barterID != None
    """

    _control: FindBarterControl = None
    _limit: int = None
    _page: int = None
    _category: str = None
    _sort: str = None
    _order: str = None
    _status: str = None
    _adminStatus: str = None

    def __init__(self, request) -> None:
        try:
            self._query = request.POST['query']
        except KeyError:
            raise RuntimeError('Missing parameter')

        assert isinstance(self._query, str), "Invalid Parameter"
        assert self._query is not ' ', "Invalid Parameter"

        try:
            self._limit = request.POST['limit']
            self._page = request.POST['page']
            self._category = request.POST['category']
            self._sort = request.POST['sort']
            self._order = request.POST['order']
            self._status = request.POST['status']
            self._adminStatus = request.POST['adminStatus']
        except KeyError:
            pass

    """ submit()
        @pre isValid() = True
        @pre isSubmitted() = False
        @post isSubmitted() = True
    """
    def find(self) -> []:
        try:
            self._control = FindBarterControl(self._query, requestedItem='Game', category=self._category, limit=self._limit, sort=self._sort,
                                              order=self._order, status=self._status, adminStatus=self._adminStatus,
                                              page=self._page)
            result: [] = self._control.execute()
        except RuntimeError as exc:
            print(exc.args)
            return exc.args

        print(result)
        return result
