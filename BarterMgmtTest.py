def m():
    print('------------------------------------------------------------')
    from BarterManagement.Boundaries.HostBarterForm import HostBarterForm
    class request:
        import datetime
        POST = {'productID':1, 'requestedItem':'Game','endDate':datetime.datetime.now() + datetime.timedelta(weeks=2)}

    form = HostBarterForm(request)
    form.submit()

    # print('------------------------------------------------------------')
    # from BarterManagement.Boundaries.PlaceOfferForm import PlaceOfferForm
    # class request:
    #     POST = {'barterID':1, 'offeredItem':'chain watch'}
    #
    # form = PlaceOfferForm(request)
    # form.submit()
    #
    # print('------------------------------------------------------------')
    # from BarterManagement.Boundaries.AcceptOfferForm import AcceptOfferForm
    # class request:
    #     POST = {'offerID':1}
    #
    # form = AcceptOfferForm(request)
    # form.submit()
    #
    # print('------------------------------------------------------------')
    #
    # from BarterManagement.Boundaries.DeclineOfferButton import DeclineOfferButton
    # class request:
    #     POST = {'offerID':1}
    #
    # form = DeclineOfferButton(request)
    # form.submit()

    from BarterManagement.Boundaries.BarterFinderService import BarterFinderService
    class request:
        POST = {'limit':30, 'page':1, 'category':'all', 'sort':'name', 'order':'desc',
                'status':'running', 'adminStatus':'active', 'query':''}

    service = BarterFinderService(request)
    service.find()
m()