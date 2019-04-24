# -*- coding: utf-8 -*-

# Copyright © 2018 by IBPort. All rights reserved.
# @Author: Neal Wong
# @Email: ibprnd@gmail.com

import os
import io

from amazon_page_parser.parsers import DetailParser

import six
import pytest

def test_parse(fr_detail_pages, fr_target_details):
    for page_path in fr_detail_pages:
        asin, _ = os.path.splitext(os.path.basename(page_path))
        target_detail = fr_target_details.get(asin, dict())
        with io.open(page_path, 'rb') as f:
            c = f.read()
            if six.PY2:
                c = unicode(c, 'utf-8')
            else:
                c = c.decode('utf-8')
            parser = DetailParser(c)

            assert parser.parse_title() == target_detail.get('title', None)
            assert set(parser.parse_author()) == set(target_detail.get('author', []))

            feature_bullets = parser.parse_feature_bullets()
            assert set(feature_bullets) == set(target_detail.get('feature_bullets', None))

            book_description = parser.parse_book_description()
            assert book_description.find(target_detail.get('book_description', '')) != -1

            product_description = parser.parse_product_description()
            assert product_description.find(target_detail.get('product_description', '')) != -1

            assert set(parser.parse_images()) == set(target_detail.get('images', []))
            assert parser.parse_star() == target_detail.get('star', 0)
            assert parser.parse_reviews() == target_detail.get('reviews', 0)
            assert parser.parse_rank() == target_detail.get('rank', 0)
            assert parser.parse_categories() == target_detail.get('categories', '')

            details = parser.parse_details()
            for k, v in target_detail.get('details', dict()).items():
                assert details.get(k, '') == v
