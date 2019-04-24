# -*- coding: utf-8 -*-

# All rights reserved.
# @Author: hyan15
# @Email: qwang16@olivetuniversity.edu

import json
import re

from parsel import Selector
from six.moves.html_parser import HTMLParser

class DetailParser(object):
    def __init__(self, text, type='html', namespaces=None, root=None, base_url=None):
        self.selector = Selector(
            text, type=type, namespaces=namespaces, root=root, base_url=base_url)
        self.html_parser = HTMLParser()

    def parse(self):
        return {
            'title': self.parse_title(),
            'author': self.parse_author(),
            'feature_bullets': self.parse_feature_bullets(),
            'book_description': self.parse_book_description(),
            'product_description': self.parse_product_description(),
            'images': self.parse_images(),
            'star': self.parse_star(),
            'reviews': self.parse_reviews(),
            'rank': self.parse_rank(),
            'categories': self.parse_categories(),
            'details': self.parse_details(),
            'bylines': self.parse_bylines()
        }

    def parse_title(self):
        raw_title = self.selector.xpath('//*[@id="productTitle"]/text()').get()
        return raw_title.strip() if raw_title else ''

    def parse_author(self):
        author_elems = self.selector.xpath('//a[@id="bylineInfo"]/text()')
        author_elems.extend(self.selector.xpath(
            '//*[@id="bylineInfo"]/span[contains(@class, "author")]/a/text()'))
        xpath_str = '//*[@id="bylineInfo"]/span[contains(@class, "author")]'
        xpath_str += '//a[contains(@class, "contributorNameID")]/text()'
        author_elems.extend(self.selector.xpath(xpath_str))
        xpath_str = '//*[@id="byline"]/span[contains(@class, "author")]'
        xpath_str += '//a[contains(@class, "contributorNameID")]/text()'
        author_elems.extend(self.selector.xpath(xpath_str))
        # xpath_str = '//*[@id="bylineInfo"]/span[contains(@class, "author")]'
        # xpath_str += '/a[contains(@class, "a-link-normal")]/text()'
        # author_elems.extend(self.selector.xpath(xpath_str))

        return author_elems.getall()

    def parse_bylines(self):
        bylines = dict()
        xpath_str = '//*[@id="bylineInfo"]/span[@class="a-color-secondary"]'
        byline_elems = self.selector.xpath(xpath_str)
        byline_elems.extend(self.selector.xpath(
            '//*[@id="bylineInfo"]/span[@class="a-color-secondary"]'))
        for byline_elem in byline_elems:
            key = byline_elem.xpath('./text()').get().strip().strip(':')
            value = byline_elem.xpath('./following-sibling::span/text()').get()
            value = value.strip() if value else ''
            if key and value:
                bylines[key] = value

        return bylines

    def parse_feature_bullets(self):
        raw_bullets = self.selector.xpath(
            '//*[@id="feature-bullets"]/ul/li/span[contains(@class, "a-list-item")]/text()').getall()
        return [s.strip().replace(u'\xa0', ' ') for s in raw_bullets if s and not s.isspace()]

    def parse_book_description(self):
        noscript_elems = self.selector.xpath('//*[@id="bookDescription_feature_div"]/noscript')
        return ''.join([s.strip() for s in noscript_elems.xpath('.//text()').getall()])

    def parse_product_description(self):
        try:
            des = self.selector.xpath('//*[@id="productDescription"]/p//text()').getall()
            product_description = ''.join([s.strip() for s in des])
        except:
            trace
            product_description = ''

        return product_description

    def parse_images(self):
        thumb_urls = []

        bottom_thumb_elems = self.selector.xpath(
            '//*[@id="imageBlockThumbs"]//div[contains(@class, "imageThumb")]/img')
        bottom_thumb_urls = bottom_thumb_elems.xpath('./@src').getall()
        thumb_urls.extend(bottom_thumb_urls)

        side_thumb_elems = self.selector.xpath(
            '//*[@id="altImages"]//li[contains(@class, "item")]//img')
        side_thumb_urls = side_thumb_elems.xpath('./@src').getall()
        thumb_urls.extend(side_thumb_urls)

        if len(thumb_urls) <= 0:
            front_img_data = self.selector.xpath(
                '//img[@id="imgBlkFront"]/@data-a-dynamic-image').get()
            if front_img_data:
                front_img_data = self.html_parser.unescape(front_img_data)
                try:
                    front_img_dict = json.loads(front_img_data)
                    thumb_urls.extend(list(front_img_dict.keys()))
                except:
                    pass

        return thumb_urls

    def parse_star(self):
        stars = 0
        stars_str = self.selector.xpath('//*[@id="acrPopover"]/@title').get()
        try:
            stars = float(stars_str.strip().split().pop(0))
        except:
            pass

        return stars

    def parse_reviews(self):
        reviews = 0
        reviews_str = self.selector.xpath(
            '//*[@id="acrCustomerReviewText"]/text()').get()
        try:
            reviews = int(reviews_str.strip().split().pop(0))
        except:
            pass

        return reviews

    def parse_details(self):
        details = dict()

        details_elems = self.selector.xpath(
            '//*[@id="productDetailsTable"]/tr/td/div[@class="content"]/ul/li[not(@id="SalesRank")]')
        for details_elem in details_elems:
            key = details_elem.xpath('./b/text()').get()
            key = key.strip().strip(':') if key else ''
            if key == 'Format':
                value = details_elem.xpath('./a/text()').get()
            elif key == 'Other Editions' or key == 'Weitere Ausgaben' or \
                key.find('Autres versions') != -1:
                value = ' | '.join(details_elem.xpath('./a/text()').getall())
            else:
                value = details_elem.xpath('./text()').get()
            value = value.strip() if value else ''
            if key and value:
                details[key] = value

        details_elems = self.selector.xpath(
            '//*[@id="detailBullets_feature_div"]/ul/li/span[@class="a-list-item"]')
        for details_elem in details_elems:
            key = details_elem.xpath('./span[@class="a-text-bold"]/text()').get()
            key = key.strip().strip(':') if key else ''
            value = details_elem.xpath(
                    './span[not(@class="a-text-bold")]/text()').get()
            value = value.strip() if value else ''
            if key and value:
                details[key] = value

        details_elems = self.selector.xpath(
            '//*[@id="productDetails_detailBullets_sections1"]/tbody/tr')
        for details_elem in details_elems:
            key = details_elem.xpath('./th/text()').get()
            key = key.strip().strip(':') if key else ''
            value = details_elem.xpath('./td/text()').get()
            value = value.strip() if value else ''
            if key and value:
                details[key] = value

        details_elems = self.selector.xpath('//div[@id="prodDetails"]//table//tr')
        for details_elem in details_elems:
            key = details_elem.xpath('./th[contains(@class, "prodDetSectionEntry")]/text()').get()
            key = key.strip().strip(':') if key else ''
            value = details_elem.xpath('./td/text()').get()
            value = value.strip() if value else ''
            if key and value:
                details[key] = value

        details_elems = self.selector.xpath(
            '//div[@id="detail-bullets"]/table/tr/td/div[@class="content"]/ul/li')
        for details_elem in details_elems:
            key = details_elem.xpath('./b/text()').get()
            key = key.strip().strip(':') if key else ''
            if key == 'Actors':
                value = ','.join(details_elem.xpath('./a/text()').getall())
            else:
                value = ''.join(details_elem.xpath('./text()').getall())
            value = value.strip() if value else ''
            if key and value:
                if key == 'Region':
                    value = value.split('(').pop(0).strip()
                details[key] = value

        details_elems = self.selector.xpath(
            '//div[@id="detail_bullets_id"]/table/tr/td/div[@class="content"]/ul/li')
        for details_elem in details_elems:
            key = details_elem.xpath('./b/text()').get()
            key = key.strip().strip(':') if key else ''
            if key == 'Other Editions' or key == 'Weitere Ausgaben' or \
                key.find('Autres versions') != -1:
                value = ' | '.join(details_elem.xpath('./a/text()').getall())
            else:
                value = ''.join(details_elem.xpath('./text()').getall())
            value = value.strip() if value else ''
            if key and value:
                details[key] = value

        details_elems = self.selector.xpath(
            '//div[@id="prodDetails"]//div[@class="pdTab"]/table//tr')
        for details_elem in details_elems:
            key = details_elem.xpath('./td[@class="label"]/text()').get()
            key = key.strip().strip(':') if key else ''
            value = details_elem.xpath('./td[@class="value"]/text()').get()
            value = value.strip() if value else ''
            if key and value:
                details[key] = value

        if 'Shipping Weight' in details:
            details['Shipping Weight'] = details['Shipping Weight'].replace(
                '(', '').replace(')', '').strip()

        if 'Region' in details:
            details['Region'] = details['Region'].split('(').pop(0).strip()

        for k in [
            'Amazon Bestsellers Rank', 'Amazon Best Sellers Rank',
            'Average Customer Review', 'Customer Reviews']:
            if k in details:
                details.pop(k)

        result = dict()
        for k, v in details.items():
            result[k.strip().replace(u'\xa0', '')] = v

        return result

    def parse_specifications(self):
        pass

    def parse_categories(self):
        categories = []
        category_wrappers = self.selector.xpath(
            '//*[@id="SalesRank"]/ul[@class="zg_hrsr"]/li')
        for category_wrapper in category_wrappers:
            categories.append('>'.join(
                category_wrapper.xpath('./span[@class="zg_hrsr_ladder"]//a/text()').getall()))

        category_wrappers = self.selector.xpath(
            '//*[@id="SalesRank"]/td[@class="value"]/ul[@class="zg_hrsr"]/li')
        for category_wrapper in category_wrappers:
            categories.append('>'.join(
                category_wrapper.xpath('./span[@class="zg_hrsr_ladder"]//a/text()').getall()))

        xpath_str = '//*[@id="prodDetails"]//table//tr'
        xpath_str += '/th[contains(@class, "prodDetSectionEntry") and '
        xpath_str += 'contains(./text(), "Best Sellers Rank")]'
        xpath_str += '/following-sibling::td'
        category_wrappers = self.selector.xpath(xpath_str).xpath('./span/span')
        try:
            category_wrappers.pop(0)
        except IndexError:
            pass
        for category_wrapper in category_wrappers:
            categories.append('>'.join(category_wrapper.xpath('./a/text()').getall()))

        return ';'.join(categories)

    def parse_rank(self):
        sales_rank_str = ''.join(
            self.selector.xpath('//*[@id="SalesRank"]/text()').getall()).strip()
        if not sales_rank_str:
            raw_sales_rank_str = ''.join(
                self.selector.xpath('//*[@id="SalesRank"]/td[@class="value"]/text()').getall())
            sales_rank_str = raw_sales_rank_str.strip()
        if sales_rank_str:
            try:
                rank = int(re.sub(r'[#,\.]', '', sales_rank_str.replace('Nr. ', '').split().pop(0)))
            except:
                rank = 0
        else:
            common_xpath_str = '//*[@id="prodDetails"]//table//tr'
            common_xpath_str += '/th[contains(@class, "prodDetSectionEntry") and '
            common_xpath_str += 'contains(./text(), "Best Sellers Rank")]/following-sibling::td'
            sales_rank_str = ''.join(
                self.selector.xpath(common_xpath_str).xpath('./span/span/text()').getall()).strip()
            if sales_rank_str:
                try:
                    rank = int(
                        re.sub(r'[#,\.]', '', sales_rank_str.replace('Nr. ', '').split().pop(0)))
                except:
                    rank = 0
            else:
                rank = 0

        return rank

class OfferListingParser(object):
    def __init__(self, text, type='html', namespaces=None, root=None, base_url=None):
        self.selector = Selector(
            text, type=type, namespaces=namespaces, root=root, base_url=base_url)
        self.html_parser = HTMLParser()

    def parse(self):
        offers = []
        offer_elems = self.selector.xpath(
            './/div[@id="olpOfferList"]//div[contains(@class, "olpOffer")]')
        for offer_elem in offer_elems:
            offer = {
                'price': self.parse_price(offer_elem),
                'shipping_price': self.parse_shipping_price(offer_elem),
                'condition_comments': self.parse_condition_comments(offer_elem),
                'available': self.parse_availability(offer_elem),
                'prime': self.parse_prime(offer_elem),
                'expected_shipping': self.parse_expected_shipping(offer_elem),
                'seller_name': self.parse_seller_name(offer_elem),
                'seller_rating': self.parse_seller_rating(offer_elem),
                'seller_feedbacks': self.parse_seller_feedbacks(offer_elem),
                'seller_stars': self.parse_seller_stars(offer_elem),
                'offer_listing_id': self.parse_offer_listing_id(offer_elem)
            }
            offer['condition'], offer['subcondition'] = self.parse_condition(offer_elem)
            offers.append(offer)

        return offers

    def parse_price(self, offer_elem):
        price = 0

        price_str = offer_elem.xpath(
            './div[contains(@class, "olpPriceColumn")]/span[contains(@class, "olpOfferPrice")]/text()').get()
        if price_str:
            price = float(re.sub(r'[^0-9\.]', '', price_str.strip().replace(',', '.')))
        else:
            raise RuntimeError('Could not find price element')

        return price

    def parse_shipping_price(self, offer_elem):
        shipping_price = 0

        prime_elem = offer_elem.xpath(
            './div[contains(@class, "olpPriceColumn")]/span[contains(@class, "supersaver")]').get()
        if prime_elem:
            return 0

        shipping_price_str = offer_elem.xpath(
            './div[contains(@class, "olpPriceColumn")]/p[@class="olpShippingInfo"]//span[@class="olpShippingPrice"]/text()').get()
        if shipping_price_str:
            return float(shipping_price_str.strip().replace('$', '').replace(',', ''))

        free_shipping_str = offer_elem.xpath(
            './div[contains(@class, "olpPriceColumn")]/p[@class="olpShippingInfo"]/span[@class="a-color-secondary"]/b/text()').get()
        if free_shipping_str:
            if free_shipping_str.lower().find('free') != -1:
                return 0

        raise RuntimeError('Could not find shipping price element')

    def parse_condition(self, offer_elem):
        condition = ''
        sub_condition = ''

        condition_elem = offer_elem.xpath(
            './div[contains(@class, "olpConditionColumn")]//span[contains(@class, "olpCondition")]')
        if not condition_elem:
            raise RuntimeError('Could not find condition element')

        id_str = condition_elem.xpath('./@id').get()
        if id_str:
            if id_str.lower().find('new') != -1:
                condition = 'New'
                sub_condition = 'New'
            elif id_str.lower().find('collectible') != -1:
                condition = 'Collectible'
                sub_condition = condition_elem.xpath(
                    './span[@id="offerSubCondition"]/text()').get().strip()
            else:
                condition = 'Used'
                sub_condition = condition_elem.xpath(
                    './span[@id="offerSubCondition"]/text()').get().strip()
        else:
            condition_strs = condition_elem.xpath('.//text()').getall()
            condition_str = [part.strip() for part in condition_strs]
            if condition_str.lower().find('new') != -1:
                condition = 'New'
                sub_condition = 'New'
            elif condition_str.lower().find('collectible') != -1:
                condition = 'Collectible'
                sub_condition = condition_elem.xpath(
                    './span[@id="offerSubCondition"]/text()').get().strip()
            else:
                conditions = [part.strip() for part in condition_str.split('-')]
                if len(conditions) > 1:
                    condition = conditions.pop(0)
                    sub_condition = conditions.pop(0)
                else:
                    condition = conditions.pop(0)
                    sub_condition = condition

        return (condition, sub_condition)

    def parse_condition_comments(self, offer_elem):
        comments = ''

        comments_elem = offer_elem.xpath(
            './div[contains(@class, "olpConditionColumn")]/div[contains(@class, "comments")]')
        if comments_elem:
            comments_wrappers = comments_elem.xpath('.//div')
            if len(comments_wrappers) > 0:
                comment_strs = comments_wrappers.xpath('./text()').getall()
                comments = ''.join([comment_str.strip() for comment_str in comment_strs])
            else:
                comments = comments_elem.xpath('./text()').get().strip()

        return comments

    def parse_availability(self, offer_elem):
        available = True

        availability_elem = offer_elem.xpath(
            './olpAvailability').get()
        if availability_elem:
            availability_str = availability_elem.xpath('./text()').get().strip()
            if availability_str:
                available = False

        return available

    def parse_prime(self, offer_elem):
        prime_elem = offer_elem.xpath(
            './div[contains(@class, "olpPriceColumn")]/span[contains(@class, "supersaver")]').get()
        return prime_elem is not None

    def parse_expected_shipping(self, offer_elem):
        shipping_content = ''.join(offer_elem.xpath(
            './div[contains(@class, "olpDeliveryColumn")]/ul[contains(@class, "olpFastTrack")]/li//text()').getall())
        expected_shipping = bool(
            re.search(r'.*(One|Two)-Day Shipping.*', shipping_content, re.M))
        expected_shipping = expected_shipping or bool(
            re.search(r'.*Expedited Shipping.*', shipping_content, re.M))
        return expected_shipping

    def parse_seller_name(self, offer_elem):
        seller_name = ''

        amazon_elem = offer_elem.xpath(
            './div[contains(@class, "olpSellerColumn")]/*[contains(@class, "olpSellerName")]//img').get()
        if amazon_elem is not None:
            return 'Amazon'

        raw_seller_name = offer_elem.xpath(
            './div[contains(@class, "olpSellerColumn")]/*[contains(@class, "olpSellerName")]//a/text()').get()
        if raw_seller_name:
            seller_name = raw_seller_name.strip()
        else:
            raise RuntimeError('Could not find seller name')

        return seller_name

    def parse_seller_rating(self, offer_elem):
        rating = 0

        rating_str = offer_elem.xpath(
            './div[contains(@class, "olpSellerColumn")]/p/a/b/text()').get()
        if rating_str:
            rating = int(rating_str.split().pop(0).replace('%', ''))
        else:
            rating = 0

        return rating

    def parse_seller_feedbacks(self, offer_elem):
        feedbacks = 0

        seller_desc_elem = offer_elem.xpath(
            './div[contains(@class, "olpSellerColumn")]/p')
        if seller_desc_elem:
            raw_seller_descs = seller_desc_elem.xpath('./text()').getall()
            seller_desc = ''.join([raw_seller_desc.strip() for raw_seller_desc in raw_seller_descs])
            if seller_desc:
                matched_feedback = re.match(r'.*\(([0-9\.,]+) total ratings\)', seller_desc)
                raw_feedbacks_str = matched_feedback.groups()[0] if matched_feedback and len(matched_feedback.groups()) > 0 else '0'
                feedbacks = int(raw_feedbacks_str.replace(',', ''))
            else:
                feedbacks = 0

        return feedbacks

    def parse_seller_stars(self, offer_elem):
        star = 0

        raw_star_str = offer_elem.xpath(
            './div[contains(@class, "olpSellerColumn")]/p/i/span/text()').get()
        if raw_star_str:
            star = float(raw_star_str.split().pop(0))
        else:
            star = 0

        return star

    def parse_offer_listing_id(self, offer_elem):
        return offer_elem.xpath(
            './div[contains(@class, "olpBuyColumn")]//form/input[@name="offeringID.1"]/@value').get()
