from StoreManagement.Entities.Category import Category
from StorageManagement.Boundaries.DatabaseConnection import DatabaseConnection
import StorageManagement.Entities.Cache as Cache
from Exceptions.DatabaseExceptions import *
from Exceptions.CategoryExceptions import *


class CategoryDAO:
    databaseTable = 'Category'
    dbConnection: DatabaseConnection = None

    def __init__(self):
        self.dbConnection = DatabaseConnection('test')

    """ create(categoryID,)
    """
    def create(self, name: str) -> int:
        data = type('dto', (object,), {})()
        data.table = self.databaseTable
        data.name = str

        try:
            newID = self.dbConnection.create(data)
        except DBEntryCreationFailException:
            raise CategoryCreationFailureException(data)

        Cache.invalidate()
        return newID

    def get(self, categoryID: int) -> Category:
        if Cache.isCached(self.databaseTable, categoryID):
            return Cache.get(self.databaseTable, categoryID)

        data = type('dto', (object,), {})()
        data.table = self.databaseTable
        data.ID = categoryID

        try:
            c = self.dbConnection.get(data)
        except DBEntryNotFoundException:
            raise CategoryNotFoundException(data)

        category = Category()
        category.setName(c['name'])
        category.setID(c['ID'])

        Cache.save(self.databaseTable, categoryID, category)
        return category

    def find(self) -> []:
        pass

    def update(self, category: Category) -> None:
        data = type('dto', (object,), {})()
        data.table = self.databaseTable
        data.ID = category.getID()
        data.name = category.getName()

        try:
            self.dbConnection.update(data)
        except DBUpdateFailException:
            raise CategoryUpdateFailureException(category)

        Cache.invalidate()

    def delete(self, categoryID: int) -> None:
        data = type('dto', (object,), {})()
        data.ID = categoryID

        try:
            self.dbConnection.delete(data)
        except DBEntryDeletionFailException:
            raise CategoryDeleteFailureException(categoryID)

        Cache.invalidate()
