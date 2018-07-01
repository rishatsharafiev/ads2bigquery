# -*- coding: utf-8 -*-

import os
import logging
import unittest
from dotenv import load_dotenv

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
DOTENV_PATH = os.path.join(BASE_PATH, '.env')
load_dotenv(DOTENV_PATH)

from google.cloud import bigquery

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
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
        FacebookAdsApi.init(
            self.FB_APP_ID,
            self.FB_APP_SECRET,
            self.FB_ACCESS_TOKEN,
        )

        # google bigquery
        self.BIGQUERY_PROJECT = os.getenv('BIGQUERY_PROJECT', '')
        # self.client = bigquery.Client(project=BIGQUERY_PROJECT)

    def test_site(self):
        my_account = AdAccount('act_106527396164822')
        campaigns = my_account.get_campaigns()
        print(campaigns)

if __name__ == '__main__':
    unittest.main()
