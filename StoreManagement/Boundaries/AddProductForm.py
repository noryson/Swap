class AddProductForm:
    #Boundary object for formatting and sanitizing new data to add to 'Store'

    productID = None
    category = None
    owner = None
    store = None
    name = None
    description = None
    productImages = []
    ownerRequest = None
    currentLocation = None

    # setters and getters

    # def process(self, request):
    #     requestProductDTO = ProductDTO()
    #     requestProductDTO.setName(request.POST['name'])
    #     requestProductDTO.setDescription(request.POST['description'])
    #     requestProductDTO.setStoreID(request.POST['storeID'])
    #
    #     addProduct = AddProductControl()
    #     addProduct.addProductToStore(requestProductDTO)

    def commit(self):
        pass