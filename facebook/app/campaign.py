# -*- coding: utf-8 -*-

import os
import logging
import unittest
from dotenv import load_dotenv

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
DOTENV_PATH = os.path.join(BASE_PATH, '.env')
load_dotenv(DOTENV_PATH)

from pydash.objects import get
from google.cloud import bigquery
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adset import AdSet
from facebook_business.exceptions import FacebookRequestError
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.user import User

class TestFacebook(unittest.TestCase):
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
        self.FACEBOOK_APP_ID = os.getenv('FACEBOOK_APP_ID', '')
        self.FACEBOOK_APP_SECRET = os.getenv('FACEBOOK_APP_SECRET', '')
        self.FACEBOOK_ACCESS_TOKEN = os.getenv('FACEBOOK_ACCESS_TOKEN', '')
        self.FACEBOOK_MARKETING_ACCOUNT = os.getenv('FACEBOOK_MARKETING_ACCOUNT', '')

        FacebookAdsApi.init(
            self.FACEBOOK_APP_ID,
            self.FACEBOOK_APP_SECRET,
            self.FACEBOOK_ACCESS_TOKEN,
        )

        # google bigquery
        self.client = bigquery.Client()

    def get_campaigns_by_account(self, account_id, fields=[]):
        account = AdAccount(account_id)
        available_fields = [attr for attr in dir(Campaign.Field) if not callable(getattr(Campaign.Field, attr)) and not attr.startswith("__")]
        include_fields = [field for field in fields if field in available_fields]

        campaigns = account.get_campaigns(fields=include_fields)

        return campaigns

    def save_campaigns(self, campaigns):
        dataset_id = self.FACEBOOK_MARKETING_ACCOUNT
        table_id = 'campaigns'
        dataset_ref = self.client.dataset(dataset_id)
        dataset = self.client.get_dataset(dataset_ref)
        table_ref = dataset_ref.table(table_id)
        table = self.client.get_table(table_ref)
        counter = 0

        for campaign in campaigns:
            # TODO: batch query by 1000 rows
            rows_to_insert = [
                (get(campaign, 'id', None), )
            ]

            print(self.client.insert_rows(table, rows_to_insert))

            counter += 1
            if counter == 3:
                break

        print('Length campaings: ', counter)

    def test_facebook(self):
        campaigns = self.get_campaigns_by_account(self.FACEBOOK_MARKETING_ACCOUNT, ['account_id', 'hello'])
        self.save_campaigns(campaigns)

if __name__ == '__main__':
    unittest.main()
