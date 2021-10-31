from copy import deepcopy


class TokenRequest(object):
    def __init__(self, project_id, user_id):
        self.__data = {
            'user': {
                'id': user_id
            },
            'settings': {
                'project_id': int(project_id)
            }
        }

    def set_user_email(self, email):
        if not isinstance(self.__data['user'].get('mail'), dict):
            self.__data['user']['email'] = {}

        self.__data['user']['email']['value'] = email
        return self

    def set_user_name(self, name):
        if not isinstance(self.__data['user'].get('name'), dict):
            self.__data['user']['name'] = {}

        self.__data['user']['name']['value'] = name
        return self

    def set_currency(self, currency):
        self.__data['settings']['currency'] = currency
        return self

    def set_custom_parameters(self, parameters):
        self.__data['custom_parameters'] = parameters
        return self

    def set_external_payment_id(self, external_id):
        self.__data['settings']['external_id'] = external_id
        return self

    def set_sandbox_mode(self, is_sandbox=True):
        self.__data['settings']['mode'] = ''
        if is_sandbox:
            self.__data['settings']['mode'] = 'sandbox'

        else:
            self.__data['settings'].pop('mode')

        return self

    def set_purchase(self, amount, currency):
        self.__data['purchase']['checkout']['amount'] = amount
        self.__data['purchase']['checkout']['currency'] = currency
        return self

    def set_user_attributes(self, attributes):
        self.__data['user']['attributes'] = attributes
        return self

    def to_json(self):
        return deepcopy(self.__data)



class PaymentUIScriptRender(object):

    @classmethod
    def send(cls, token, is_sandbox=False):
        return cls.render(token, is_sandbox)

    @classmethod
    def render(cls, token, is_sandbox=False):
        template = '''
<script>
    var options = {
        access_token: "%s",
        sandbox: %s
    };
    var s = document.createElement('script');
    s.type = "text/javascript";
    s.async = true;
    s.src = "//static.xsolla.com/embed/paystation/1.0.7/widget.min.js";
    s.addEventListener('load', function (e) {
        XPayStationWidget.init(options);
    }, false);
    var head = document.getElementsByTagName('head')[0];
    head.appendChild(s);
</script>
        '''
        sandbox = 'true' if is_sandbox else 'false'
        return template % (token, sandbox)
