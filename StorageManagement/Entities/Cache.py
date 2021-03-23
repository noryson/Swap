barter = dict()
offer = dict()
proof = dict()
status = 'invalid'


def get(table, idn):
    if table == 'Barter':
        print('Data retrieved from barter cache.')
        return barter[idn]

    if table == 'Offer':
        print('Data retrieved from offer cache.')
        return offer[idn]


def save(table, idn, entity):
    if table == 'Barter':
        barter[idn] = entity
        validate()
        print('Barter has been cached.')

    if table == 'Offer':
        offer[idn] = entity
        validate()
        print('Offer has been cached.')


def validate():
    setStatus('valid')


def invalidate():
    setStatus('invalid')
    global barter
    global offer
    global proof
    barter = dict()
    offer = dict()
    proof = dict()


def isCached(table, idn):
    if not isValid():
        return False

    if table == 'Barter':
        try:
            barter[idn]
        except KeyError:
            return False
        return True

    if table == 'Offer':
        try:
            offer[idn]
        except KeyError:
            return False
        return True


def isValid() -> bool:
    if getStatus() == 'valid':
        return True
    else:
        return False


def printCache():
    print(barter)
    print('----------------------\n')
    print(offer)
    print('----------------------\n')
    print(proof)
    print('----------------------\n')


def getStatus() -> str:
    return status


def setStatus(newStatus) -> None:
    global status
    status = newStatus