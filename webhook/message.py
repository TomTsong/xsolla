from abc import ABCMeta
from copy import deepcopy
from xsolla.exceptions.webhook import InvalidParameterException


class Message(metaclass=ABCMeta):
    USER_VALIDATION = 'user_validation'
    USER_SEARCH = 'user_search'
    PAYMENT = 'payment'
    REFUND = 'refund'
    CREATE_SUBSCRIPTION = 'create_subscription'
    CANCEL_SUBSCRIPTION = 'cancel_subscription'
    UPDATE_SUBSCRIPTION = 'update_subscription'
    USER_BALANCE = 'user_balance_operation'
    GET_PIN_CODE = 'get_pincode'
    AFS_REJECT = 'afs_reject'

    class_map = {
        USER_VALIDATION: 'UserValidationMessage',
        USER_SEARCH: 'UserSearchMessage',
        PAYMENT: 'PaymentMessage',
        REFUND: 'RefundMessage',
        CREATE_SUBSCRIPTION: 'CreateSubscriptionMessage',
        CANCEL_SUBSCRIPTION: 'CancelSubscriptionMessage',
        UPDATE_SUBSCRIPTION: 'UpdateSubscriptionMessage',
        USER_BALANCE: 'UserBalanceMessage',
        GET_PIN_CODE: 'GetPinCodeMessage',
        AFS_REJECT: 'AfsRejectMessage'
    }

    @classmethod
    def from_dict(cls, request):
        if 'notification_type' not in request:
            raise InvalidParameterException('notification_type key not found in Xsolla webhook request')

        notification_type = request['notification_type']
        if notification_type not in class_map:
            raise InvalidParameterException(f'Unknown notification_type in Xsolla webhook request: {notification_type}')

        klass = eval(class_map[notification_type])
        return klass(request)

    def __init__(self, request):
        self.request = deepcopy(request)

    def to_dict(self):
        return self.request

    def get_notification_type(self):
        return self.request['notification']

    def is_user_validation(self):
        return self.USER_VALIDATION == self.get_notification_type()

    def is_payment(self):
        return self.PAYMENT == self.get_notification_type()

    def is_refund(self):
        return self.REFUND == self.get_notification_type()

    def get_user_id(self):
        return self.request['user']['id']


class AfsRejectMessage(Message):
    def get_transaction(self):
        return self.request['transaction']

    def get_payment_id(self):
        return self.request['transaction']['id']

    def get_external_payment_id(self):
        if 'external_id' in self.request['transaction']:
            return self.request['transaction']['external_id']

        return None

    def get_payment_agreement(self):
        return self.request['transaction']['agreement']

    def get_refund_details(self):
        return self.request['refund_details']


class CancelSubscriptionMessage(Message):
    def get_subscription(self):
        return self.request['subscription']


class CreateSubscriptionMessage(CancelSubscriptionMessage):
    def get_coupon(self):
        if 'coupon' not in self.request:
            return {}

        return self.request['coupon']


class GetPinCodeMessage(Message):
    def get_digital_content(self):
        return self.request['pin_code']['digital_content']

    def get_DRM(self):
        return self.request['pin_code']['DRM']


class PaymentMessage(Message):
    def get_purchase(self):
        return self.request['purchase']

    def get_transaction(self):
        return self.request['transaction']

    def get_payment_id(self):
        return self.request['transaction']['id']

    def get_external_payment_id(self):
        if 'external_id' in self.request['transaction']:
            return self.request['transaction']['external_id']

        return None

    def get_payment_details(self):
        return self.request['payment_details']

    def get_custom_parameters(self):
        if 'custom_parameters' not in self.request:
            return {}

        return self.request['custom_parameters']

    def is_dry_run(self):
        if 'dry_run' not in self.request['transaction']:
            return False

        return bool(self.request['transaction']['dry_run'])


class RefundMessage(PaymentMessage):
    def get_refund_details(self):
        return self.request['refund_details']
    

class UpdateSubscriptionMessage(CancelSubscriptionMessage):
    pass


class UserBalanceMessage(Message):
    PAYMENT = 'payment'
    IN_GAME_PURCHASE = 'inGamePurchase'
    COUPON = 'coupon'
    INTERNAL = 'internal'
    CANCELLATION = 'cancellation'

    def get_virtual_currency_balance(self):
        if 'virtual_currency_balance' not in self.request:
            return {}

        return self.request['virtual_currency_balance']

    def get_operation_type(self):
        return self.request['operation_type']

    def get_operation_id(self):
        return self.request['id_operation']

    def get_coupon(self):
        if 'coupon' not in self.request:
            return {}

        return self.request['coupon']

    def get_items_operation_type(self):
        if 'items_operation_type' in self.request:
            return self.request['items_operation_type']

        return None

    
class UserSearchMessage(Message):
    def get_user_public_id(self):
        if 'public_id' in self.request['user']:
            return self.request['user']['public_id']

        return None

    def get_user_id(self):
        if 'id' in self.request['user']:
            return self.request['user']['id']

        return None


class UserValidationMessage(Message):
    pass
