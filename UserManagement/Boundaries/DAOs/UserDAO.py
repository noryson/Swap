import datetime
from StorageManagement.Boundaries.DatabaseConnection import DatabaseConnection
import StorageManagement.Entities.Cache as Cache
from UserManagement.Entities.DjangoUser import DjangoUser as User
from Exceptions.UserExceptions import *
from Exceptions.DatabaseExceptions import *


class UserDAO:

    """ invariants:
        @inv getDatabaseTable() = 'User'
        @inv getdbConnection() != None
    """
    databaseTable = 'User'
    dbConnection = None

    def __init__(self):
        self.dbConnection = DatabaseConnection('test')

    """ create(userDTO)
        @pre userDTO.getProduct().getUser() = None or product.canHostUser = True
        @pre userDTO.getProduct().getUser() != None
    """
    def create(self, productID: int, requestedItem: str, endDate: datetime.datetime):
        # data = type('dto', (object,), {})()
        # data.productID = productID
        # data.requestedItem = requestedItem
        # data.endDate = endDate
        # data.table = self.databaseTable
        #
        # try:
        #     newID = self.dbConnection.create(data)
        # except DBEntryCreationFailException:
        #     raise UserCreationFailException(data)
        #
        # Cache.invalidate()
        # return newID
        pass

    """ get(userDTO)
        @pre userDTO.getID() != None
    """
    def get(self, userID: int) -> User:
        if Cache.isCached(self.databaseTable, userID):
            return Cache.get(self.databaseTable, userID)

        data = type('dto', (object,), {})()
        data.table = self.databaseTable
        data.ID = userID

        user: User = User()
        try:
            from django.contrib.auth.models import User as DUser
            u = DUser.objects.get(pk=userID)
        except DBEntryNotFoundException:
            raise UserNotFoundException(userID)

        # user = User()
        # user.setID(u['ID'])
        # user.setFirstName(u['firstName'])
        # user.setLastName(u['lastName'])
        # user.setEmail(u['email'])
        # user.setOnline(u['online'])
        # user.setRole(u['role'])
        # user.setSecret(u['secret'])
        # user.setActive(u['active'])
        # user.setVerified(u['verified'])
        # user.setVerificationToken(u['verificationToken'])
        # user.setDate(u['date'])
        # user.setLastLogin(u['lastLogin'])
        # user.setStoreID(u['storeID'])
        # # user.setReports
        # user.setProfileImageID(u['profileImageID'])
        # user.setChatIDs(u['chatIDs'])
        # user.setSubscriptionIDs(u['subscriptionIDs'])
        # user.setGroups(u['groups'])

        user.setUser(u)
        Cache.save(self.databaseTable, userID, u)
        return u

    """ search(userDTO)
        @pre userDTO != empty
    """
    def find(self, productName, requestedItem=None, category=None, limit=30, page=1, status=None, adminStatus=None,
             sort=None, order=None, startDate: datetime.datetime = None, endDate: datetime.datetime = None) -> []:
        pass

    """ update(userDTO)
        @pre userDTO.getID() != None
    """
    def update(self, user: User) -> None:
        # data = type('dto', (object,), {})()
        # data.table = self.databaseTable
        # data.ID = user.getID()
        # data.requestedItem = user.getRequest()
        # data.maxNoOfOffers = user.getMaxNoOfOffers()
        # data.endDate = user.getEndDate()
        # data.status = user.getStatus()
        # data.adminStatus = user.getAdminStatus()
        # # data.productID = user.getProduct().getID()
        #
        # try:
        #     self.dbConnection.update(data)
        # except DBUpdateFailException:
        #     raise UserUpdateFailureException(user)

        user.getUser().save()
        Cache.invalidate()

    """ delete(userDTO)
        @pre userDTO.getID() != None
    """
    def delete(self, userID) -> None:
        # data = type('dto', (object,), {})()
        # data.ID = userID
        #
        # try:
        #     self.dbConnection.delete(data)
        # except DBEntryDeletionFailException:
        #     raise UserDeleteFailureException(userID)
        #
        # Cache.invalidate()
        pass

