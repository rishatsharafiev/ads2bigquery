# -*- coding: utf-8 -*-

import os
import logging
import unittest
from dotenv import load_dotenv

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
DOTENV_PATH = os.path.join(BASE_PATH, '.env')
load_dotenv(DOTENV_PATH)

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

    def create_dataset(self, dataset_id):
        dataset_ref = self.client.dataset(dataset_id)
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = 'US'
        dataset = self.client.create_dataset(dataset)

    def list_datasets(self):
        client = self.client
        datasets = list(client.list_datasets())
        project = client.project

        if datasets:
            print('Datasets in project {}:'.format(project))
            for dataset in datasets:  # API request(s)
                print('\t{}'.format(dataset.dataset_id))
        else:
            print('{} project does not contain any datasets.'.format(project))

    def test_site(self):
        # self.create_dataset('test1')
        self.list_datasets()


if __name__ == '__main__':
    unittest.main()
