from StoreManagement.Entities.Product import Product
from StorageManagement.Boundaries.DatabaseConnection import DatabaseConnection
import StorageManagement.Entities.Cache as Cache
from Exceptions.DatabaseExceptions import *
from Exceptions.ProductExceptions import *


class ProductDAO:
    #Data Access Objects of the 'Product' entity into the database

    databaseTable = 'Product'
    dbConnection: DatabaseConnection = None

    def __init__(self):
        self.dbConnection = DatabaseConnection('test')

    """ create(storeID,)
    """
    def create(self, storeID: int, name: str, description: str, location: str, categoryID: int, imageIDs: []) -> int:
        data = type('dto', (object,), {})()
        data.table = self.databaseTable
        data.storeID = storeID
        data.categoryID = categoryID
        data.name = name
        data.description = description
        data.location = location
        data.imageIDs = imageIDs

        try:
            newID = self.dbConnection.create(data)
        except DBEntryCreationFailException:
            raise ProductCreationFailedException(data)

        Cache.invalidate()
        return newID

    def get(self, productID) -> Product:
        if Cache.isCached(self.databaseTable, productID):
            return Cache.get(self.databaseTable, productID)

        data = type('dto', (object,), {})()
        data.table = self.databaseTable
        data.ID = productID

        try:
            p = self.dbConnection.get(data)
        except DBEntryNotFoundException:
            raise ProductNotFoundException(data)

        product = Product()
        product.setID(p['ID'])
        product.setName(p['name'])
        product.setDescription(p['description'])
        product.setLocation(p['location'])
        product.setDate(p['creationDate'])
        product.setImageIDs(p['imageIDs'])
        product.setBarterIDs(p['barterIDs'])

        from StoreManagement.Entities.CategoryProxy import CategoryProxy
        category = CategoryProxy()
        category.setRealCategoryID(p['categoryID'])
        product.setCategory(category)

        from StoreManagement.Entities.StoreProxy import StoreProxy
        store = StoreProxy()
        store.setRealStoreID(p['storeID'])
        product.setStore(store)

        Cache.save(self.databaseTable, productID, product)
        return product

    def find(self) -> []:
        pass

    def update(self, product: Product) -> None:
        data = type('dto', (object,), {})()
        data.table = self.databaseTable
        data.ID = product.getID()
        data.name = product.getName()
        data.description = product.getDescription()
        data.location = product.getLocation()
        data.categoryID = product.getCategory().getID()
        data.storeID = product.getStore().getID()
        data.imageIDs = product.getImageIDs()
        data.barterIDs = product.getBarterIDs()

        try:
            self.dbConnection.update(data)
        except DBUpdateFailException:
            raise ProductUpdateFailureException(product)

        Cache.invalidate()

    def delete(self, productID: int) -> None:
        data = type('dto', (object,), {})()
        data.ID = productID

        try:
            self.dbConnection.delete(data)
        except DBEntryDeletionFailException:
            raise ProductDeleteFailureException(productID)

        Cache.invalidate()
