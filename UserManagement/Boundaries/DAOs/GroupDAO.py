import datetime
from StorageManagement.Boundaries.DatabaseConnection import DatabaseConnection
import StorageManagement.Entities.Cache as Cache
from UserManagement.Entities.DjangoGroup import DjangoGroup as Group
from Exceptions.GroupExceptions import *
from Exceptions.DatabaseExceptions import *


class GroupDAO:

    """ invariants:
        @inv getDatabaseTable() = 'Group'
        @inv getdbConnection() != None
    """
    databaseTable = 'Group'
    dbConnection = None

    def __init__(self):
        self.dbConnection = DatabaseConnection('test')

    """ create(groupDTO)
        @pre groupDTO.getProduct().getGroup() = None or product.canHostGroup = True
        @pre groupDTO.getProduct().getGroup() != None
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
        #     raise GroupCreationFailException(data)
        #
        # Cache.invalidate()
        # return newID
        pass

    """ get(groupDTO)
        @pre groupDTO.getID() != None
    """
    def get(self, groupID: int) -> Group:
        if Cache.isCached(self.databaseTable, groupID):
            return Cache.get(self.databaseTable, groupID)

        data = type('dto', (object,), {})()
        data.table = self.databaseTable
        data.ID = groupID

        group: Group = Group()
        try:
            from django.contrib.auth.models import Group as DGroup
            u = DGroup.objects.get(pk=groupID)
        except DBEntryNotFoundException:
            raise GroupNotFoundException(groupID)

        # group = Group()
        # group.setID(u['ID'])
        # group.setFirstName(u['firstName'])
        # group.setLastName(u['lastName'])
        # group.setEmail(u['email'])
        # group.setOnline(u['online'])
        # group.setRole(u['role'])
        # group.setSecret(u['secret'])
        # group.setActive(u['active'])
        # group.setVerified(u['verified'])
        # group.setVerificationToken(u['verificationToken'])
        # group.setDate(u['date'])
        # group.setLastLogin(u['lastLogin'])
        # group.setStoreID(u['storeID'])
        # # group.setReports
        # group.setProfileImageID(u['profileImageID'])
        # group.setChatIDs(u['chatIDs'])
        # group.setSubscriptionIDs(u['subscriptionIDs'])
        # group.setGroups(u['groups'])

        group.setGroup(u)
        Cache.save(self.databaseTable, groupID, u)
        return u

    """ search(groupDTO)
        @pre groupDTO != empty
    """
    def find(self, productName, requestedItem=None, category=None, limit=30, page=1, status=None, adminStatus=None,
             sort=None, order=None, startDate: datetime.datetime = None, endDate: datetime.datetime = None) -> []:
        pass

    """ update(groupDTO)
        @pre groupDTO.getID() != None
    """
    def update(self, group: Group) -> None:
        # data = type('dto', (object,), {})()
        # data.table = self.databaseTable
        # data.ID = group.getID()
        # data.requestedItem = group.getRequest()
        # data.maxNoOfOffers = group.getMaxNoOfOffers()
        # data.endDate = group.getEndDate()
        # data.status = group.getStatus()
        # data.adminStatus = group.getAdminStatus()
        # # data.productID = group.getProduct().getID()
        #
        # try:
        #     self.dbConnection.update(data)
        # except DBUpdateFailException:
        #     raise GroupUpdateFailureException(group)

        group.getGroup().save()
        Cache.invalidate()

    """ delete(groupDTO)
        @pre groupDTO.getID() != None
    """
    def delete(self, groupID) -> None:
        # data = type('dto', (object,), {})()
        # data.ID = groupID
        #
        # try:
        #     self.dbConnection.delete(data)
        # except DBEntryDeletionFailException:
        #     raise GroupDeleteFailureException(groupID)
        #
        # Cache.invalidate()
        pass

