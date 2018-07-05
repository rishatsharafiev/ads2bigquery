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

    def create_dataset(self, dataset_id):
        client = self.client
        exists = [dataset.dataset_id for dataset in client.list_datasets()]
        try:
            if dataset_id not in exists:
                dataset_ref = client.dataset(dataset_id)
                dataset = bigquery.Dataset(dataset_ref)
                dataset.location = 'US'
                dataset = client.create_dataset(dataset)
                print('{dataset_id} is created'.format(dataset_id=dataset_id))
            else:
                print('{dataset_id} dataset exists'.format(dataset_id=dataset_id))
        except exceptions.Conflict as e:
            print(str(e))
        finally:
            pass

    def create_table(self, dataset_id, table_id, fields=[]):
        client = self.client
        dataset_ref = client.dataset(dataset_id)
        exists = [table.table_id for table in list(client.list_tables(dataset_ref))]
        try:
            if table_id not in exists:
                schema = []
                [schema.append(bigquery.SchemaField(field, 'STRING')) for field in fields]

                table_ref = dataset_ref.table(table_id)
                table = bigquery.Table(table_ref, schema=schema)
                table = client.create_table(table)
            else:
                print('{table_id} table exists'.format(table_id=table_id))
        except exceptions.Conflict as e:
            print(str(e))
        finally:
            pass

    def test_site(self):
        self.create_dataset(self.FACEBOOK_MARKETING_ACCOUNT)

        self.create_table(dataset_id=self.FACEBOOK_MARKETING_ACCOUNT, table_id='campaigns', fields=[
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

if __name__ == '__main__':
    unittest.main()
