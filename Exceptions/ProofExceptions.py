class ProofException(BaseException):
    pass


class ProofIsConfirmedException(ProofException):
    pass


class ProofNotConfirmedException(ProofException):
    pass


class ProofNotFoundException(ProofException):
    pass


class ProofMaxExceededException(ProofException):
    pass
