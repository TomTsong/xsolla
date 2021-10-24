from xsolla.exceptions.xsolla import XsollaException


class AccessDeniedException(XsollaException):
    pass


class UnprocessableEntityException(XsollaException):
    pass
