# -*- coding: utf-8 -*-

# Copyright :copyright: 2019 by IBPort. All rights reserved.
# @Author: Neal Wong
# @Email: ibprnd@gmail.com

import os
import codecs

from amazon_page_parser.store_front_parser import StoreFrontParser

import six
import pytest

@pytest.fixture(scope='module')
def store_front_pages(us_pages_dir):
    pages = []
    page_path = os.path.join(us_pages_dir, 'store_front.html')
    with codecs.open(page_path, 'rb') as f:
        c = f.read()
        if six.PY2:
            c = unicode(c, 'utf-8')
        else:
            c = c.decode('utf-8')

        pages.append(c)

    yield pages

@pytest.fixture(scope='module')
def target_store_front_products():
    return [
        {
            'asins': [
                'B07Y4Z6LBD', 'B07TYWF8K7', 'B083KDYS6W', 'B00VG1AHLE',
                'B083W9P5S1', 'B07WPBVBDY', 'B07R3G7NZN', 'B07SQXTJBR',
                'B07VKKLHS6', 'B07ST8Z9PQ', 'B07X8GLFLR', 'B07WY5D2LQ',
                'B07STBBGJW', 'B07VRZT8BM', 'B07PY6J9VH', 'B07Z5L6WZX'
            ],
            'next_page_url': '/s?i=merchant-items&me=A2DP2EEPU3VU45&page=2&marketplaceID=ATVPDKIKX0DER&qid=1591913227&ref=sr_pg_1'
        }
    ]

def test_parse(store_front_pages, target_store_front_products):
    products = []
    for store_front_page in store_front_pages:
        parser = StoreFrontParser(store_front_page)
        products.append(parser.parse())

    for store_front_products_by_page in target_store_front_products:
        assert store_front_products_by_page in products
