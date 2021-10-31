import re

from xsolla.exceptions.webhook import InvalidClientIpException, InvalidSignatureException


class User(object):
    def __init__(self, id, name=None, public_id=None, email=None, phone=None):
        self.id = id
        self.public_id = public_id
        self.name = name
        self.email = email
        self.phone = phone

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
        return self

    def get_public_id(self):
        return self.public_id

    def set_public_id(self, public_id):
        self.public_id = public_id
        return self

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return self

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
        return self

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone
        return self

    def to_json(self):
        user = {}
        if self.id:
            user['id'] = self.id

        if self.name:
            user['name'] = self.name

        if self.public_id:
            user['public_id'] = self.public_id

        if self.email:
            user['email'] = self.email

        if self.phone:
            user['phone'] = self.phone

        return user


class WebhookRequest(object):
    codes = [
        JSON_ERROR_CTRL_CHAR => 'Control character error, possibly incorrectly encoded.',
        JSON_ERROR_DEPTH => 'The maximum stack depth has been exceeded.',
        JSON_ERROR_NONE => 'No error has occurred.',
        JSON_ERROR_STATE_MISMATCH => 'Invalid or malformed JSON.',
        JSON_ERROR_SYNTAX => 'Syntax error.',
        JSON_ERROR_UTF8 => 'Malformed UTF-8 characters, possibly incorrectly encoded.',
    ]

    def __init__(self, headers, body, client_ip=None):
        self.headers = headers
        self.body = body
        self.client_ip = client_ip

    def get_body(self):
        return self.body

    def get_headers(self):
        return self.headers

    def get_client_ip(self):
        return self.client_ip

    def to_json(self):
        data = json.decode(self.body)
        return data


class WebhookAuthenticator(object):
    xsolla_subnets = [
        '159.255.220.240/28',
        '185.30.20.16/29',
        '185.30.21.0/24',
        '185.30.21.16/29',
    ]

    def __init__(self, project_secret_key):
        self.project_secret_key = project_secret_key

    def authenticate(self, webhook_request: WebhookRequest, check_client_ip=True):
        if True == check_client_ip:
            self.authenticate_client_ip(webhook_request.get_client_ip())

        self.authenticate_signature(webhook_request)

    def authenticate_client_ip(self, client_ip):
        if False == IpUtils.check_ip(client_ip, self.xsolla_subnets):
            raise InvalidClientIpException(
                    'Client IP address (%s) not found in allowed IP addresses whitelist (%s). Please check troubleshooting section in README.md https://github.com/xsolla/xsolla-sdk-php#troubleshooting' % (
                    client_ip, ', '.join(self.xsolla_subnets))
                )

    def authenticate_signature(self, webhook_request: WebhookRequest):
        headers = webhook_request.get_headers()
        if 'Authorization' not in headers:
            raise InvalidSignatureException(
                '"Authorization" header not found in Xsolla webhook request. Please check troubleshooting section in README.md https://github.com/xsolla/xsolla-sdk-php#troubleshooting'
            )

        match = re.search('^Signature ([0-9a-f]{40})$', headers['Authorization'])
        if not match:
            raise InvalidSignatureException(
                'Signature not found in "Authorization" header from Xsolla webhook request: ' + headers['Authorization']
            )

        client_signature = match.group(1)
        server_signature = sha1(webhook_request.get_body() + bytes(self.project_secret_key))
        if client_signature != server_signature:
            raise InvalidSignatureException(
                "Invalid Signature. Signature provided in \"Authorization\" header ($clientSignature) does not match with expected"
            )
