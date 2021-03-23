import datetime
import StorageManagement.Entities.Cache as Cache
from StorageManagement.Boundaries.DatabaseConnection import DatabaseConnection
from StoreManagement.Entities.Store import Store
from Exceptions.DatabaseExceptions import *
from Exceptions.StoreExceptions import *


class StoreDAO:
    databaseTable = 'Store'
    dbConnection: DatabaseConnection = None

    def __init__(self):
        self.databaseSystem = DatabaseConnection('test')

    """ create(ownerID)
        @pre userService.hasStore(ownerID) == False
        @post userService.hasStore(ownerID) == True
    """
    def create(self, ownerID: int, maxNoOfProducts: int) -> int:
        data = type('dto', (object,), {})()
        data.ownerID = ownerID
        data.maxNoOfProducts = maxNoOfProducts
        data.table = self.databaseTable

        try:
            newID = self.dbConnection.create(data)
        except DBEntryCreationFailException:
            raise StoreCreationFailedException(data)

        Cache.invalidate()
        return newID

    def get(self, storeID: int) -> Store:
        if Cache.isCached(self.databaseTable, storeID):
            return Cache.get(self.databaseTable, storeID)

        data = type('dto', (object,), {})()
        data.table = self.databaseTable
        data.ID = storeID

        try:
            s = self.dbConnection.get(data)
        except DBEntryNotFoundException:
            raise StoreNotFoundException(data)

        store = Store()
        store.setID(s['ID'])
        store.setOwnerID(s['ownerID'])
        store.setStatus(s['status'])
        store.setSubscriberIDs(s['subscriberIDs'])
        store.setMaxNoOfProducts(s['maxNoOfProducts'])
        store.setDate(s['creationDate'])

        products: [] = list()
        from StoreManagement.Entities.ProductProxy import ProductProxy
        for productID in s['productIDs']:
            product: ProductProxy = ProductProxy()
            product.setRealProductID(productID)
            products.append(product)
        store.setProducts(products)

        Cache.save(self.databaseTable, storeID, store)
        return store

    def find(self) -> []:
        pass

    def update(self, store: Store) -> None:
        data = type('dto', (object,), {})()
        data.table = self.databaseTable
        data.ID = store.getID()
        data.maxNoOfProducts = store.getMaxNoOfProducts()
        data.status = store.getStatus()
        data.subscriberIDs = store.getSubscriberIDs()
        data.productIDs = list()
        for product in store.getProducts():
            data.productIDs.append(product.getID())

        try:
            self.dbConnection.update(data)
        except DBUpdateFailException:
            raise StoreUpdateFailureException(store)

        Cache.invalidate()

    def delete(self, storeID: int) -> None:
        data = type('dto', (object,), {})()
        data.ID = storeID

        try:
            self.dbConnection.delete(data)
        except DBEntryDeletionFailException:
            raise StoreDeleteFailureException(storeID)

        Cache.invalidate()
