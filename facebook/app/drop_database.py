# -*- coding: utf-8 -*-

import os
import logging
import unittest
from dotenv import load_dotenv

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
DOTENV_PATH = os.path.join(BASE_PATH, '.env')
load_dotenv(DOTENV_PATH)

from google.api_core import exceptions
from google.cloud import bigquery

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

        # google bigquery
        self.client = bigquery.Client()
        self.FACEBOOK_MARKETING_ACCOUNT = os.getenv('FACEBOOK_MARKETING_ACCOUNT', '')

    def drop_dataset(self, dataset_id):
        client = self.client
        exists = [dataset.dataset_id for dataset in client.list_datasets()]
        try:
            if dataset_id in exists:
                dataset_ref = client.dataset(dataset_id)
                client.delete_dataset(dataset_ref, delete_contents=True)
                print('{dataset_id} dataset is deleted'.format(dataset_id=dataset_id))
            else:
                print('{dataset_id} dataset not exists'.format(dataset_id=dataset_id))
        except exceptions.Conflict as e:
            print(str(e))
        finally:
            pass

    def test_site(self):
        self.drop_dataset(self.FACEBOOK_MARKETING_ACCOUNT)

if __name__ == '__main__':
    unittest.main()
