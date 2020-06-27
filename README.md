amazon-page-parser
=====================

Currently supported detail fields are:
* title - Title
* author - Array of authors
* feature_bullets - Array of feature bullets
* book_description - description under offer information
* product_description - description under editorial review
* images - Array of images
* star - Average star of custom reviews
* reviews - Custom Reviews count
* rank - Sales Rank in top browse node
* categories - Browse nodes trees, multiple tree pathes are concated by ';'
* details - Details are key, value pairs.

Offer listing fields are:
* star - Average star of custom reviews
* reviews - Custom reviews count
* offers
    * price - Product price
    * shipping_price - Shipping price
    * condition - Condition
    * subcondition - Subcondition
    * condition_comments - Condition comments
    * available - Whether product is currently available, or needs pre-ordered
    * prime - Whether shipping supports prime options
    * expected_shipping - Whether shipping support expected options
    * seller_name - Seller name
    * seller_id - Seller ID
    * seller_rating - Seller rating
    * seller_feedbacks - Seller feedback count
    * seller_stars - Seller stars count
    * offer_listing_id - Offer listing ID

Tracking fields are:
* carrier - Carrier name
* tracking_id - Tracking number
* is_shipped - Whether order is shipped


Store Front fields are:
* asins - Store front asins in page
* next_page_url - Next page url path


Installation
-------------

The simplest way is to install it via `devpi`:

    devpi install amazon-page-parser


Run Test
-------------

`devpi install -r requirements-dev.txt`

`tox`
