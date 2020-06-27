# -*- coding: utf-8 -*-

# All rights reserved.
# @Author: hyan15
# @Email: qwang16@olivetuniversity.edu

import os
import codecs

from amazon_page_parser.parsers import OfferListingParser

import six
import pytest

@pytest.fixture(scope='module')
def shared_context():
    base_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pages', 'us')

    context = dict()

    page_path = os.path.join(base_path, 'offer_listing_0001982389.html')
    context['0001982389'] = {
        'page_path': page_path,
        'offer_listing': {
            'star': 0,
            'reviews': 0,
            'offers': [
                {
                    'price': 5.99,
                    'shipping_price': 0,
                    'condition_comments': '',
                    'available': True,
                    'prime': False,
                    'expected_shipping': True,
                    'condition': 'Used',
                    'subcondition': 'Good',
                    'seller_name': 'owlsbooks',
                    'seller_id': 'A1TJP2EKS10VL4',
                    'seller_rating': 95,
                    'seller_feedbacks': 623885,
                    'seller_stars': 5,
                    'offer_listing_id': 'vH6NvFomyBg24shPK8GYT%2FgM0UzWJ9Q7BwSHtReq4UVyd%2ByU7%2B8ndHow5O4DAOVDv8GzAk4z4k7v%2BnFjxx3jiwLCJNJ5AKbYsvhUNlfwWoMGlEyhLtpluTzR0e%2FyEjbfCfoTDrFZMyY%2BNwFTMuxjNgHRYf4wQRgB',
                },
                {
                    'price': 5.99,
                    'shipping_price': 0,
                    'condition_comments': '',
                    'available': True,
                    'prime': False,
                    'expected_shipping': True,
                    'condition': 'Used',
                    'subcondition': 'Good',
                    'seller_name': 'greattimebooks',
                    'seller_id': 'A16ET7DS3ZNK1W',
                    'seller_rating': 95,
                    'seller_feedbacks': 122425,
                    'seller_stars': 5,
                    'offer_listing_id': 'vH6NvFomyBg24shPK8GYT%2FgM0UzWJ9Q7%2F78etAcqbFCHWPiFO8En3x1B3bVD94AboQhh5dHUaolJNyacKURWK8vvQPFaarWJqhCe4JQWw1xDflRZFu%2FdLVkrkAUHsJLfvCfLdfPGA5MDfT9iLYjzpg%3D%3D',
                },
                {
                    'price': 2.0,
                    'shipping_price': 3.99,
                    'condition_comments': '',
                    'available': True,
                    'prime': False,
                    'expected_shipping': False,
                    'condition': 'Used',
                    'subcondition': 'Good',
                    'seller_name': 'ALEXTHEFATDAWG-US',
                    'seller_id': 'A2RFJF90LNL7PE',
                    'seller_rating': 93,
                    'seller_feedbacks': 7096,
                    'seller_stars': 4.5,
                    'offer_listing_id': 'vH6NvFomyBg24shPK8GYT%2FgM0UzWJ9Q7jOc0MxOZT%2B2IzyCsOLPmrC8hyqvBmx2i1I6uSN0jQXkvIehvnq9NMSvCyRhrfto9d2tEsUvLeSQybPvwN2b4R2GzLMSNaz%2FAaV%2BtFrxDW%2FVRK%2B6mdR0mWQ%3D%3D',
                },
                {
                    'price': 5.99,
                    'shipping_price': 0,
                    'condition_comments': '',
                    'available': True,
                    'prime': False,
                    'expected_shipping': True,
                    'condition': 'Used',
                    'subcondition': 'Good',
                    'seller_name': 'ThriftBooks - Motor City',
                    'seller_id': 'A1QJ4UH6FW3UH1',
                    'seller_rating': 93,
                    'seller_feedbacks': 531979,
                    'seller_stars': 4.5,
                    'offer_listing_id': 'vH6NvFomyBg24shPK8GYT%2FgM0UzWJ9Q70j%2FhxcvnzhTZv1JldM9HO2BFOsqNPrrQYoDbsOh7qUYFQeyCL%2Fnwast68fv4pZN3jtPUo6MLH0Yyqx8sH1JrAdwCATpR7SpaHF00CTecoqU%3D',
                },
                {
                    'price': 5.99,
                    'shipping_price': 0,
                    'condition_comments': '',
                    'available': True,
                    'prime': False,
                    'expected_shipping': True,
                    'condition': 'Used',
                    'subcondition': 'Good',
                    'seller_name': '-bearbooks-',
                    'seller_id': 'A2ENLOCYXEFS31',
                    'seller_rating': 94,
                    'seller_feedbacks': 274071,
                    'seller_stars': 4.5,
                    'offer_listing_id': 'vH6NvFomyBg24shPK8GYT%2FgM0UzWJ9Q7jDtLiBBbi62hV%2BiDcpMkOZHGYq72MAk6lke85k%2Ftj8IgMaG0PiIpB6bnioIAvgfOSXj%2F8%2BFAqwtvxElXs23RZ4tVGLHimpyNQkYKBXnkH8liwnuYs0mnzA%3D%3D',
                },
                {
                    'price': 5.99,
                    'shipping_price': 0,
                    'condition_comments': '',
                    'available': True,
                    'prime': False,
                    'expected_shipping': True,
                    'condition': 'Used',
                    'subcondition': 'Acceptable',
                    'seller_name': 'Thriftbooks',
                    'seller_id': 'A365C2XG0O7B0H',
                    'seller_rating': 93,
                    'seller_feedbacks': 993843,
                    'seller_stars': 4.5,
                    'offer_listing_id': 'vH6NvFomyBg24shPK8GYT%2FgM0UzWJ9Q7h2MbhKoRXfTYm%2B6o98%2BHN57rYi%2BKdULjVblO05%2FIHpVaf4y0zsveI85hqSJxZzMuFmf6tnti4vChjhJb3pJN%2FduSS%2BZT8ovz8dh2Mg7eSNl4Eusu6VuMTQ%3D%3D',
                },
                {
                    'price': 2.95,
                    'shipping_price': 3.99,
                    'condition_comments': '',
                    'available': True,
                    'prime': False,
                    'expected_shipping': False,
                    'condition': 'Used',
                    'subcondition': 'Good',
                    'seller_name': 'greener_books_london',
                    'seller_id': 'A161AAYHQBTAQT',
                    'seller_rating': 91,
                    'seller_feedbacks': 59148,
                    'seller_stars': 4.5,
                    'offer_listing_id': 'vH6NvFomyBg24shPK8GYT%2FgM0UzWJ9Q7foTgGHe2emCI7ap1HvsA3av53LxnLt6nXfvcti3s5CG1NVAOvEj4SLUD9VZmxvGxJZVaqT5hnIojJdF1IO%2FHOx6v%2BhJ5ESFg5NEWEnCKH4X56Hf9xkluzw%3D%3D',
                },
                {
                    'price': 3.0,
                    'shipping_price': 3.99,
                    'condition_comments': '',
                    'available': True,
                    'prime': False,
                    'expected_shipping': False,
                    'condition': 'Used',
                    'subcondition': 'Very Good',
                    'seller_name': 'worldofbooksusa',
                    'seller_id': 'A2W0XT7SMZ33XS',
                    'seller_rating': 88,
                    'seller_feedbacks': 391289,
                    'seller_stars': 4.5,
                    'offer_listing_id': 'vH6NvFomyBg24shPK8GYT%2FgM0UzWJ9Q786rC9w0YHr6gC8c3G%2F9BbbjmkDIo2JYD5MJ8e4eLjIILqB9yBXn1jBlKeqiPTorSEIGQobbdEZ6VNee54YhpUMfoOErOsTmLv3o9m4Lbjs3CdlW8yy6wfjL%2FfFNcvdYN',
                },
                {
                    'price': 12.12,
                    'shipping_price': 0,
                    'condition_comments': '',
                    'available': True,
                    'prime': False,
                    'expected_shipping': True,
                    'condition': 'Used',
                    'subcondition': 'Good',
                    'seller_name': 'GlassFrogBooks',
                    'seller_id': 'A2LAZA9IUFPA4W',
                    'seller_rating': 94,
                    'seller_feedbacks': 2578,
                    'seller_stars': 4.5,
                    'offer_listing_id': 'vH6NvFomyBg24shPK8GYT%2FgM0UzWJ9Q7%2FjSX%2FI9I%2Fp9sSqfsT2VPHcw%2BDiJk5ct7qKMp%2B7ZbY7yxJG6N9ACyVNTj2BCiJlVL9R1spmxnqwn5fflGpcV%2FCuV7Mm5aafOnpHNO38RSsQywxyhMT8ZLwQCBFsx9hsGh',
                },
                {
                    'price': 8.0,
                    'shipping_price': 4.14,
                    'condition_comments': '',
                    'available': True,
                    'prime': False,
                    'expected_shipping': False,
                    'condition': 'Used',
                    'subcondition': 'Good',
                    'seller_name': 'American Book Center',
                    'seller_id': 'A3RS1FL91NCFWQ',
                    'seller_rating': 62,
                    'seller_feedbacks': 382,
                    'seller_stars': 3.5,
                    'offer_listing_id': 'vH6NvFomyBg24shPK8GYT%2FgM0UzWJ9Q7FQMCIhMk5tBfDCURwYya%2Bolf1hJWl%2Fr%2B%2F6uafJwuYiANaFKxr4%2BVb0%2F7p%2BvbSh68liN0sJ692pXhuxG54vZfLqlmTaAao1IRj8zHWFzky756su1egKYOflF9YJ%2BfvVLn',
                }
            ]
        }
    }

    with codecs.open(page_path, encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if six.PY2:
            c = unicode(c)
        context['0001982389']['parser'] = OfferListingParser(c)

    context['B07L6P7J2M'] = {
        'page_path': os.path.join(base_path, 'offer_listing_B07L6P7J2M.html'),
        'offer_listing': {
            'star': 4.6,
            'reviews': 7821,
            'offers': [
                {
                    'price': 19.99,
                    'shipping_price': 0,
                    'condition_comments': '',
                    'available': True,
                    'prime': True,
                    'expected_shipping': False,
                    'condition': 'New',
                    'subcondition': 'New',
                    'seller_name': 'Oasis1270',
                    'seller_id': 'A1WNZAYT9WQDYM',
                    'seller_rating': 97,
                    'seller_feedbacks': 1720,
                    'seller_stars': 5,
                    'offer_listing_id': 'JrBIhSNqXuxG1m3PRlri9GRpv80XDGa3H71sPrnXzDx%2F4pHOfbeYbPF%2Bg9redP%2F7g4KwqubncedDRweXNBX1hRYz5fHVJv03UrDgCs%2BFRfQfFtnahYkOo1SiJF1Cfd6pRA9UfEK5G65TGyGCXh3BzLS1KogmtEE0eqaCx1O3G58BbwHMN7rLnI%2FGwUgpBQfS',
                },
                {
                    'price': 24.99,
                    'shipping_price': 0,
                    'condition_comments': '',
                    'available': True,
                    'prime': True,
                    'expected_shipping': False,
                    'condition': 'New',
                    'subcondition': 'New',
                    'seller_name': 'RULTO',
                    'seller_id': 'APF0ST32AI5H2',
                    'seller_rating': 92,
                    'seller_feedbacks': 26,
                    'seller_stars': 4.5,
                    'offer_listing_id': 'JrBIhSNqXuxG1m3PRlri9GRpv80XDGa3nInxOR6Eu1k%2FygS7xUxq%2FPKlL9MfjKmxfR0Sx0rboYY4DQowBM3ltt5jBWlWNwf8GuKz5Jqfy9yZgavUz4PByu07TutucGnAjYYsAbIHjhgoWlf9GbxUtH1UUYUj3VG3vGP3pPG40KdGvz9NUmoQKK8eCdPNFRve',
                },
                {
                    'price': 29.99,
                    'shipping_price': 0,
                    'condition_comments': '',
                    'available': True,
                    'prime': True,
                    'expected_shipping': False,
                    'condition': 'New',
                    'subcondition': 'New',
                    'seller_name': 'Novilex',
                    'seller_id': 'AYDAPDJLLWM0W',
                    'seller_rating': 97,
                    'seller_feedbacks': 515,
                    'seller_stars': 5,
                    'offer_listing_id': 'JrBIhSNqXuxG1m3PRlri9GRpv80XDGa3rD%2BYEeXGJaXovoIt5uS3OCYTLyp6EPBO7or39TVRd2lfkr3fRBTu8fP2bChO8feA3uXqrRa1%2BAjI3BFKdv58%2B25ak01uNxkNjk7cgL%2Bz4zYT7lOxv%2BcGUqTxCkaRF5FuTEE4%2FUAQZcn5tq8rhJYchwk7rRxsahk2',
                },
            ]
        }
    }

    with codecs.open(context['B07L6P7J2M']['page_path'], encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if six.PY2:
            c = unicode(c)
        context['B07L6P7J2M']['parser'] = OfferListingParser(c)

    yield context

def test_parse(shared_context):
    for k, v in shared_context.items():
        parser = v['parser']
        target_offer_listing = v['offer_listing']
        offer_listing = parser.parse()
        assert offer_listing['star'] == target_offer_listing['star']
        assert offer_listing['reviews'] == target_offer_listing['reviews']

        for idx, offer in enumerate(target_offer_listing['offers']):
            o = offer_listing['offers'][idx]
            assert o['price'] == offer['price']
            assert o['shipping_price'] == offer['shipping_price']
            assert o['available'] == offer['available']
            assert o['prime'] == offer['prime']
            assert o['expected_shipping'] == offer['expected_shipping']
            assert o['condition'] == offer['condition']
            assert o['subcondition'] == offer['subcondition']
            assert o['seller_name'] == offer['seller_name']
            assert o['seller_rating'] == offer['seller_rating']
            assert o['seller_feedbacks'] == offer['seller_feedbacks']
            assert o['seller_stars'] == offer['seller_stars']
            assert o['offer_listing_id'] == offer['offer_listing_id']
