# -*- coding: utf-8 -*-

# Copyright :copyright: 2019 by IBPort. All rights reserved.
# @Author: Neal Wong
# @Email: ibprnd@gmail.com

import json
import re

from parsel import Selector
from six.moves.html_parser import HTMLParser


class StoreFrontParser(object):
    def __init__(self, text, type='html', namespaces=None, root=None, base_url=None):
        self.selector = Selector(
            text, type=type, namespaces=namespaces, root=root, base_url=base_url)
        self.html_parser = HTMLParser()

    def parse(self):
        asins = []
        products_container_xpath = '//div[contains(@class, "s-result-list") and contains(@class, "s-main-slot")]'
        products_container_elem = self.selector.xpath(products_container_xpath)
        for product_elem in products_container_elem.xpath('./div[@data-asin]'):
            asin = product_elem.xpath('./@data-asin').get()
            if asin:
                asins.append(asin)

        next_page_elem = products_container_elem.xpath(
            './/ul[contains(@class, "a-pagination")]/li/a[contains(text(), "Next")]')
        if next_page_elem:
            next_page_url = self.html_parser.unescape(next_page_elem.xpath('./@href').get())
        else:
            next_page_url = None

        return {'asins': asins, 'next_page_url': next_page_url}
