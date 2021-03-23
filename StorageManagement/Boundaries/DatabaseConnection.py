from StorageManagement.Entities.DatabaseInterface import DatabaseInterface
from Exceptions.DatabaseExceptions import *


class DatabaseConnection:
    _dbEngine: DatabaseInterface = None

    def __init__(self, env=None):
        if env == 'test':
            from StorageManagement.Entities.DummyDB import DummyDB
            self._dbEngine = DummyDB()
        else:
            raise RuntimeError('Database Engine not linked')

    def create(self, data) -> int:
        try:
            self._dbEngine.open()
            newID = self._dbEngine.create(data)
            self._dbEngine.close()
        except ConnectionError:
            raise DBEntryCreationFailException

        return newID

    def get(self, data):
        try:
            self._dbEngine.open()
            result = self._dbEngine.get(data)
            self._dbEngine.close()
        except ConnectionError:
            raise DBEntryNotFoundException

        return result

    def find(self, data):
        try:
            self._dbEngine.open()
            result: [] = self._dbEngine.find(data)
            self._dbEngine.close()
        except ConnectionError:
            raise DBEntryNotFoundException

        return result

    def update(self, data):
        try:
            self._dbEngine.open()
            self._dbEngine.update(data)
            self._dbEngine.close()
        except ConnectionError:
            raise DBUpdateFailException

    def delete(self, data):
        try:
            self._dbEngine.open()
            self._dbEngine.delete(data)
            self._dbEngine.close()
        except ConnectionError:
            raise DBEntryDeletionFailException(data)

    def setDatabaseEngine(self, newDBEngine):
        self._dbEngine.close()
        self._dbEngine = newDBEngine



