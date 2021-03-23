from StoreManagement.Entities.StoreProxy import StoreProxy
from StoreManagement.Entities.CategoryProxy import CategoryProxy
from StoreManagement.Boundaries.DAOs.ProductDAO import ProductDAO
from Exceptions.StoreExceptions import *
from Exceptions.CategoryExceptions import *
from FileManagement.Boundaries.Validator import Validator
from FileManagement.Boundaries.Uploader import Uploader
from Exceptions.FileExceptions import *


class AddProductControl:
    """" invariants:
    """
    _store: StoreProxy = None
    _name: str = None
    _description: str = None
    _location: str = None
    _categoryID: int = None
    _fileDTOs: [] = list()

    def __init__(self, storeID: int, name: str, description: str, location: str, categoryID: int, files: []) -> None:
        try:
            storeProxy: StoreProxy = StoreProxy()
            storeProxy.setRealStoreID(storeID)
            storeProxy.proxyCheck()

            categoryProxy: CategoryProxy = CategoryProxy()
            categoryProxy.setRealCategoryID(categoryID)
            categoryProxy.proxyCheck()
        except StoreNotFoundException:
            raise RuntimeError("store not found" + str(storeID))
        except CategoryNotFoundException:
            raise RuntimeError("category not existing" + str(categoryID))

        try:
            validator = Validator()
            for file in files:
                validator.validate(file, 'image')
        except FileTypeException:
            raise RuntimeError('Invalid file')

        self._store = storeProxy
        self._name = name
        self._description = description
        self._location = location

    ''' addProductToStore()
        @pre store.isActive() == True
        @pre !Product.isExisting(product)
        @post Product.isExisting(product)
    '''
    def execute(self) -> None:
        if not self._store.isActive():
            raise StoreIsDeactivatedException(self._store)

        try:
            fileIDs = list()
            for file in self._fileDTOs:
                uploader = Uploader()
                fileID = uploader.upload(file)
                fileIDs.append(fileID)
        except FileUploadException:
            raise RuntimeError('Upload failed')

        dao = ProductDAO()
        dao.create(self._store.getID(), self._name, self._description, self._location, self._categoryID, fileIDs)

    #call notification, suscribers
    def notifySuscribers(self):
        pass
