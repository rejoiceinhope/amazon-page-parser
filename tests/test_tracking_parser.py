# -*- coding: utf-8 -*-

# Copyright :copyright: 2019 by IBPort. All rights reserved.
# @Author: Neal Wong
# @Email: ibprnd@gmail.com

import os
import io

from amazon_page_parser.tracking_parser import TrackingParser

import six
import pytest

def test_parse(tracking_pages, target_trackings):
    trackings = []
    for tracking_page in tracking_pages:
        with io.open(tracking_page, 'rb') as f:
            c = f.read()
            if six.PY2:
                c = unicode(c, 'utf-8')
            else:
                c = c.decode('utf-8')
            parser = TrackingParser(c)
            trackings.append(parser.parse())

    assert len(trackings) == len(target_trackings)
    for tracking in trackings:
        assert tracking in target_trackings
