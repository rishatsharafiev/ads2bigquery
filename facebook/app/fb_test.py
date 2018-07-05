# -*- coding: utf-8 -*-

import os
import logging
import unittest
from dotenv import load_dotenv

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
DOTENV_PATH = os.path.join(BASE_PATH, '.env')
load_dotenv(DOTENV_PATH)

from pydash.objects import get
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign as AdCampaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.exceptions import FacebookRequestError
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.user import User

class TestSite(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger(__name__)
        logger_path = os.getenv('LOG_PATH', '')
        logger_handler = logging.FileHandler(os.path.join(logger_path, '{}.log'.format(__name__)))
        logger_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        logger_handler.setFormatter(logger_formatter)
        self.logger.addHandler(logger_handler)
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        # facebook marketing api
        self.FB_APP_ID = os.getenv('FB_APP_ID', '')
        self.FB_APP_SECRET = os.getenv('FB_APP_SECRET', '')
        self.FB_ACCESS_TOKEN = os.getenv('FB_ACCESS_TOKEN', '')
        self.FB_MARKETING_ACCOUNT = os.getenv('FB_MARKETING_ACCOUNT', '')

        FacebookAdsApi.init(
            self.FB_APP_ID,
            self.FB_APP_SECRET,
            self.FB_ACCESS_TOKEN,
        )

        # google bigquery
        self.BIGQUERY_PROJECT = os.getenv('BIGQUERY_PROJECT', '')
        # self.client = bigquery.Client(project=BIGQUERY_PROJECT)

    def get_campaigns_by_account(self, account_id):
        account = AdAccount(account_id)
        campaigns = account.get_campaigns(fields=[
            'account_id',
            'adlabels',
            'bid_strategy',
            'brand_lift_studies',
            'budget_remaining',
            'buying_type',
            'configured_status',
            'created_time',
            'daily_budget',
            'effective_status',
            'id',
            'name',
            'objective',
            'recommendations',
            'start_time',
            'status',
            'stop_time',
            'updated_time',
            'adbatch',
            'execution_options',
        ])

        counter = 0
        for campaign in campaigns:
            # print(ad_sets)
            print('name: ', get(campaign, 'name', ''))
            counter += 1

        print('Length campaings: ', counter)

    def get_ad_sets_by_account(self, account_id):
        account = AdAccount(account_id)
        ad_sets = account.get_ad_sets(fields=[
            'account_id',
            'adlabels',
            'adset_schedule',
            'attribution_spec',
            'bid_amount',
            'bid_info',
            'bid_strategy',
            'billing_event',
            'budget_remaining',
            'campaign',
            'campaign_id',
            'configured_status',
            'created_time',
            'creative_sequence',
            'daily_budget',
            'daily_min_spend_target',
            'daily_spend_cap',
            'destination_type',
            'effective_status',
            'end_time',
            'frequency_control_specs',
            'instagram_actor_id',
            'lifetime_budget',
            'lifetime_imps',
            'ifetime_min_spend_target',
            'lifetime_spend_cap',
            'name',
            'optimization_goal',
            'pacing_type',
            'promoted_object',
            'recommendations',
            'recurring_budget_semantics',
            'rtb_flag',
            'source_adset',
            'start_time',
            'status',
            'targeting',
            'updated_time',
            'campaign_spec',
            # 'daily_imps',
            'execution_options'
        ])

        counter = 0
        for ad_set in ad_sets:
            # print(ad_sets)
            print('name: ', get(ad_set, 'name', ''))
            counter += 1

        print('Length adsets: ', counter)

    def get_ads(self, account_id):
        account = AdAccount(account_id)
        ads = account.get_ads(fields=[
            'account_id',
            'ad_review_feedback',
            'adlabels',
            'adset',
            'adset_id',
            'bid_amount',
            'bid_info',
            'bid_type',
            'campaign',
            'campaign_id',
            'configured_status',
            'conversion_specs',
            'created_time',
            'creative',
            'effective_status',
            'id',
            'last_updated_by_app_id',
            'name',
            'recommendations',
            'source_ad',
            'source_ad_id',
            'status',
            'tracking_specs',
            'updated_time',
            'adset_spec',
            'date_format',
            'display_sequence',
            'execution_options',
            'filename',
        ])

        counter = 0
        for ad in ads:
            # print(ad_sets)
            print('name: ', get(ad, 'name', ''))
            counter += 1

        print('Length ads: ', counter)

    def test_fb(self):
        pass
        # self.get_campaigns_by_account(self.FB_MARKETING_ACCOUNT)
        # self.get_ad_sets_by_account(self.FB_MARKETING_ACCOUNT)
        # self.get_ads(self.FB_MARKETING_ACCOUNT)


if __name__ == '__main__':
    unittest.main()
