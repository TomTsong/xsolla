from xsolla.exceptions.xsolla import XsollaException


class XsollaWebhookException(XsollaException):
    xsolla_error_code = 'SERVER_ERROR'
    http_status_code = 500

    @classmethod
    def get_xsolla_error_code(cls):
        return cls.xsolla_error_code

    @classmethod
    def get_http_status_code(cls):
        return cls.http_status_code


class ClientErrorException(XsollaWebhookException):
    xsolla_error_code = 'CLIENT_ERROR'
    http_status_code = 400


class InvalidAmountException(ClientErrorException):
    xsolla_error_code = 'INCORRECT_AMOUNT'
    http_status_code = 422


class InvalidClientIpException(ClientErrorException):
    xsolla_error_code = 'INVALID_CLIENT_IP'
    http_status_code = 401


class InvalidInvoiceException(ClientErrorException):
    xsolla_error_code = 'INCORRECT_INVOICE'
    http_status_code = 422


class InvalidParameterException(ClientErrorException):
    xsolla_error_code = 'INVALID_PARAMETER'
    http_status_code = 422


class InvalidSignatureException(ClientErrorException):
    xsolla_error_code = 'INVALID_SIGNATURE'
    http_status_code = 401


class InvalidUserException(ClientErrorException):
    xsolla_error_code = 'INVALID_USER'
    http_status_code = 422


class ServerErrorException(XsollaWebhookException):
    pass
