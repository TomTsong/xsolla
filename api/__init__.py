import json
import requests

from xsolla.api.payment_ui import TokenRequest


class XsollaClient(object):
    merchant_id = None

    def create_payment_u_i_token(self, args = []):
        pass

    def create_subscription_plan(self, args = []):
        pass

    def update_subscription_plan(self, args = []):
        pass

    def list_subscription_plans(self, args = []):
        pass

    def create_subscription_product(self, args = []):
        pass

    def update_subscription_product(self, args = []):
        pass

    def list_subscription_products(self, args = []):
        pass

    def update_subscription(self, args = []):
        pass

    def list_subscriptions(self, args = []):
        pass

    def list_subscription_payments(self, args = []):
        pass

    def list_user_subscription_payments(self, args = []):
        pass

    def list_subscription_currencies(self, args = []):
        pass

    def list_user_attributes(self, args = []):
        pass

    def get_user_attribute(self, args = []):
        pass

    def create_user_attribute(self, args = []):
        pass

    def create_virtual_item(self, args = []):
        pass

    def get_virtual_item(self, args = []):
        pass

    def list_virtual_items(self, args = []):
        pass

    def create_virtual_items_group(self, args = []):
        pass

    def get_virtual_items_group(self, args = []):
        pass

    def list_virtual_items_groups(self, args = []):
        pass

    def get_project_virtual_currency_settings(self, args = []):
        pass

    def get_wallet_user(self, args = []):
        pass

    def list_wallet_users(self, args = []):
        pass

    def list_wallet_user_operations(self, args = []):
        pass

    def recharge_wallet_user_balance(self, args = []):
        pass

    def list_wallet_user_virtual_items(self, args = []):
        pass

    def get_coupon(self, args = []):
        pass

    def redeem_coupon(self, args = []):
        pass

    def create_promotion(self, args = []):
        pass

    def get_promotion(self, args = []):
        pass

    def review_promotion(self, args = []):
        pass

    def list_promotions(self, args = []):
        pass

    def get_promotion_subject(self, args = []):
        pass

    def get_promotion_payment_systems(self, args = []):
        pass

    def get_promotion_periods(self, args = []):
        pass

    def get_promotion_rewards(self, args = []):
        pass

    def list_coupon_promotions(self, args = []):
        pass

    def create_coupon_promotion(self, args = []):
        pass

    def list_events(self, args = []):
        pass

    def search_payments_registry(self, args = []):
        pass

    def list_payments_registry(self, args = []):
        pass

    def list_transfers_registry(self, args = []):
        pass

    def list_reports_registry(self, args = []):
        pass

    def list_support_tickets(self, args = []):
        pass

    def list_support_ticket_comments(self, args = []):
        pass

    def create_game_delivery_entity(self, args = []):
        pass

    def get_game_delivery_entity(self, args = []):
        pass

    def list_game_delivery_entities(self, args = []):
        pass

    def list_game_delivery_drm_platforms(self, args = []):
        pass

    def get_storefront_virtual_currency(self, args = []):
        pass

    def get_storefront_virtual_groups(self, args = []):
        pass

    def get_storefront_virtual_items(self, args = []):
        pass

    def get_storefront_subscriptions(self, args = []):
        pass

    def get_storefront_bonus(self, args = []):
        pass

    def create_project(self, args = []):
        pass

    def get_project(self, args = []):
        pass

    def list_projects(self, args = []):
        pass

    def list_payment_accounts(self, args = []):
        pass

    def charge_payment_account(self, args = []):
        pass

    def delete_payment_account(self, args = []):
        pass    

    def create_payment_ui_token_from_request(self, token_request: TokenRequest):
        ############################################################
        res = self.create_payment_ui_token(token_request.to_dict())
        return res['token']
        ############################################################

    def create_common_payment_ui_token(self, project_id, user_id, sandbox_mode=False):
        token_request = TokenRequest(project_id, user_id)
        token_request.set_sandbox_mode(sandbox_mode)
        return self.create_payment_ui_token_from_request(token_request)
