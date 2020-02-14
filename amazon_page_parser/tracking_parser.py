# -*- coding: utf-8 -*-

# Copyright :copyright: 2019 by IBPort. All rights reserved.
# @Author: Neal Wong
# @Email: ibprnd@gmail.com

import json
import re

from parsel import Selector
from six.moves.html_parser import HTMLParser


class TrackingParser(object):
    def __init__(self, text, type='html', namespaces=None, root=None, base_url=None):
        self.selector = Selector(
            text, type=type, namespaces=namespaces, root=root, base_url=base_url)
        self.html_parser = HTMLParser()
        self.xpathes = {
            'carrier': '//div[@id="carrierRelatedInfo-container"]//*[contains(text(), "Shipped with") or contains(text(), "Delivery by")]/text()',
            'tracking_id': '//div[@id="carrierRelatedInfo-container"]//*[contains(text(), "Tracking ID:")]/text()',
            'is_shipped': '//div[@id="progressTracker-container"]//div[@data-start="SHIPPED" and @data-reached="reached"]',
            'is_out_for_delivery': '//div[@id="progressTracker-container"]//div[@data-start="OUT_FOR_DELIVERY" and @data-reached="reached"]',
            'is_delivered': '//span[contains(@class, "milestone-primaryMessage") and contains(text(), "Delivered")]'
        }

    def parse(self):
        return {
            'carrier': self.parse_carrier(),
            'tracking_id': self.parse_tracking_id(),
            'is_shipped': self.parse_is_shipped() or self.parse_is_delivered()
        }

    def parse_is_shipped(self):
        return self.selector.xpath(self.xpathes['is_shipped']).get() is not None

    def is_out_for_delivery(self):
        return self.selector.xpath(self.xpathes['is_out_for_delivery']).get() is not None

    def parse_is_delivered(self):
        return self.selector.xpath(self.xpathes['is_delivered']).get() is not None

    def parse_tracking_id(self):
        tracking_id_text = self.selector.xpath(self.xpathes['tracking_id']).get()
        if tracking_id_text:
            tracking_id = tracking_id_text.replace('Tracking ID:', '').strip()
        else:
            tracking_id = None

        return tracking_id

    def parse_carrier(self):
        carrier_text = self.selector.xpath(self.xpathes['carrier']).get()
        if carrier_text:
            carrier = carrier_text.replace('Shipped with', '').replace('Delivery by', '').strip()
        else:
            carrier = None

        return carrier
