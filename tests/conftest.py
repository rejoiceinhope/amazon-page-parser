# -*- coding: utf-8 -*-

# Copyright © 2018 by IBPort. All rights reserved.
# @Author: Neal Wong
# @Email: ibprnd@gmail.com

import os
from glob import glob

import pytest

@pytest.fixture(scope='session')
def uk_pages_dir():
    return os.path.join(os.path.dirname(__file__), 'pages', 'uk')

@pytest.fixture(scope='session')
def uk_detail_pages(uk_pages_dir):
    return glob(os.path.join(uk_pages_dir, 'details', '*.html'))

@pytest.fixture(scope='session')
def us_pages_dir():
    return os.path.join(os.path.dirname(__file__), 'pages', 'us')

@pytest.fixture(scope='session')
def us_detail_pages(us_pages_dir):
    return glob(os.path.join(us_pages_dir, 'details', '*.html'))

@pytest.fixture(scope='session')
def ca_pages_dir():
    return os.path.join(os.path.dirname(__file__), 'pages', 'ca')

@pytest.fixture(scope='session')
def ca_detail_pages(ca_pages_dir):
    return glob(os.path.join(ca_pages_dir, 'details', '*.html'))

@pytest.fixture(scope='session')
def de_pages_dir():
    return os.path.join(os.path.dirname(__file__), 'pages', 'de')

@pytest.fixture(scope='session')
def de_detail_pages(de_pages_dir):
    return glob(os.path.join(de_pages_dir, 'details', '*.html'))

@pytest.fixture(scope='session')
def fr_pages_dir():
    return os.path.join(os.path.dirname(__file__), 'pages', 'fr')

@pytest.fixture(scope='session')
def fr_detail_pages(fr_pages_dir):
    return glob(os.path.join(fr_pages_dir, 'details', '*.html'))

@pytest.fixture(scope='session')
def it_pages_dir():
    return os.path.join(os.path.dirname(__file__), 'pages', 'it')

@pytest.fixture(scope='session')
def it_detail_pages(it_pages_dir):
    return glob(os.path.join(it_pages_dir, 'details', '*.html'))

@pytest.fixture(scope='session')
def es_pages_dir():
    return os.path.join(os.path.dirname(__file__), 'pages', 'es')

@pytest.fixture(scope='session')
def es_detail_pages(es_pages_dir):
    return glob(os.path.join(es_pages_dir, 'details', '*.html'))

@pytest.fixture(scope='session')
def us_target_details():
    return {
        '0062796984': {
            'title': 'The Confidence Code for Girls: Taking Risks, Messing Up, and Becoming Your Amazingly Imperfect, Totally Powerful Self',
            'author': ['Katty Kay', 'Claire Shipman', 'JillEllyn Riley', 'Nan Lawson'],
            'bylines': {},
            'feature_bullets': [],
            'book_description': 'Girls can rule the world',
            'product_description': '',
            'images': ['https://images-na.ssl-images-amazon.com/images/I/518yJPrEaxL._AC_SX60_CR,0,0,60,60_.jpg'],
            'star': 5.0,
            'reviews': 11,
            'rank': 5,
            'categories': "Books>Children's Books>Growing Up & Facts of Life>Friendship, Social Skills & School Life>Girls & Women;Books>Children's Books>Growing Up & Facts of Life>Friendship, Social Skills & School Life>Self-Esteem & Self-Respect;Books>Children's Books>Growing Up & Facts of Life>Friendship, Social Skills & School Life>Emotions & Feelings",
            'details': {
                'Age Range': '8 - 12 years',
                'Grade Level': '3 - 7',
                'Hardcover': '320 pages',
                'Publisher': 'HarperCollins (April 3, 2018)',
                'Language': 'English',
                'ISBN-10': '0062796984',
                'ISBN-13': '978-0062796981',
                'Product Dimensions': '5.5 x 1 x 8.2 inches',
                'Shipping Weight': '1 pounds'
            }
        },
        '0131103628': {
            'title': 'C Programming Language, 2nd Edition',
            'author': ['Brian W. Kernighan', 'Dennis M. Ritchie'],
            'bylines': {},
            'feature_bullets': [],
            'book_description': "The authors present the complete guide to ANSI standard C language programming. Written by the developers of C, this new version helps readers keep up with the finalized ANSI standard for C while showing how to take advantage of C's rich set of operators, economy of expression, improved control flow, and data structures.",
            'product_description': '',
            'images': ['https://images-na.ssl-images-amazon.com/images/I/41gHB8KelXL._SX258_BO1,204,203,200_.jpg', 'https://images-na.ssl-images-amazon.com/images/I/41gHB8KelXL._SX377_BO1,204,203,200_.jpg'],
            'star': 4.6,
            'reviews': 621,
            'rank': 5838,
            'categories': "Books>Computers & Technology>Programming>Languages & Tools>C & C++>C;Books>Textbooks>Computer Science>Programming Languages;Books>Computers & Technology>Software",
            'details': {
                'Paperback': '272 pages',
                'Publisher': 'Prentice Hall; 2 edition (April 1, 1988)',
                'Language': 'English',
                'ISBN-10': '0131103628',
                'ISBN-13': '978-0131103627',
                'Product Dimensions': '6.9 x 0.8 x 9.1 inches',
                'Shipping Weight': '1.2 pounds'
            }
        },
        '1439878676': {
            'title': 'Hydroponic Food Production: A Definitive Guidebook for the Advanced Home Gardener and the Commercial Hydroponic Grower, Seventh Edition',
            'author': ['Howard M. Resh'],
            'bylines': {},
            'feature_bullets': [],
            'book_description': "Hydroponic Food Production: A Definitive Guidebook for the Advanced Home Gardener and the Commercial Hydroponic Grower",
            'product_description': '',
            'images': ['https://images-na.ssl-images-amazon.com/images/I/51brbbNH1wL._SY344_BO1,204,203,200_.jpg', 'https://images-na.ssl-images-amazon.com/images/I/51brbbNH1wL._SX348_BO1,204,203,200_.jpg'],
            'star': 4.3,
            'reviews': 53,
            'rank': 301800,
            'categories': "Books>Science & Math>Agricultural Sciences>Agronomy;Books>Science & Math>Agricultural Sciences>Horticulture;Books>Textbooks>Science & Mathematics>Biology & Life Sciences>Botany",
            'details': {
                'Hardcover': '560 pages',
                'Publisher': 'CRC Press; 7 edition (August 9, 2012)',
                'Language': 'English',
                'ISBN-10': '1439878676',
                'ISBN-13': '978-1439878675',
                'Product Dimensions': '7.2 x 1.2 x 10.2 inches',
                'Shipping Weight': '2.5 pounds'
            }
        },
        'B01GAWQSFW': {
            'title': 'Simple Leather Vintage Female Quartz Watch Wristwatch Black',
            'author': ['LinTimes'],
            'bylines': {},
            'feature_bullets': [
                'Vintage bracelet wrist watch for women or ladies.100% brand new with fabulous appearance.',
                'Thickness:5mm, Dial diameter:23mm,Buckle and case material:Stainless Steel',
                'Unique design;Naturally beautiful and durable. Very Lightweight and comfortable on the wrist.',
                'Suits for ladies girls, family members, holiday gifts, festival gifts, other etc.',
                'Nice present for yourself or your friends.'
            ],
            'book_description': "",
            'product_description': 'Stylish and high quality Fashion Watch',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/41ZKssAM9zL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41d5dTDS7SL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41sKncb2bjL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/513k1k3BhxL._SR38,50_.jpg'
            ],
            'star': 3.9,
            'reviews': 12,
            'rank': 103676,
            'categories': "Clothing, Shoes & Jewelry>Women>Watches>Wrist Watches;Clothing, Shoes & Jewelry>Women>Shops",
            'details': {
                'Package Dimensions': '4.2 x 3.9 x 1.9 inches',
                'Shipping Weight': '0.8 ounces',
                'ASIN': 'B01GAWQSFW',
                'Item model number': '4331797957',
                'Date first listed on Amazon': 'May 28, 2016'
            }
        },
        'B01LW7X0JJ': {
            'title': 'uxcell Stretch Spandex Short Dining Chair Covers Slipcovers Parson Chair Covers White + Black',
            'author': ['uxcell'],
            'bylines': {},
            'feature_bullets': [
                'High stretchable fabric chair covers, it can protect your furniture from spills, stains, wear and tear, they are Environmental and healthy.',
                'Wrinkle Resistant: Chair Slipcovers can secure fit with sewn-in elastic hem and cover your chairs quickly, bring a new face to your chair.',
                'Machine wash separately. Do not bleach. Tumble dry low. Not Ironing. Dining Chair Slipcover is fadeless and pilling resistance for long-lasting durability.',
                'Applicable Occasions: Chair covers are stylish and elegant design, it is perfect for home decor kitchen, bedroom, living room, office or meeting room, hotel, wedding banquet, celebration and ceremony.',
                u"Size: Chair-back height 18-24'' and chair-back width 15-19''. Chair seat width and length 15-19'' and thickness 1.5-4''. If you have any issue with chair cover, do not hesitate to contact us as your satisfaction is the most important. We’ll take care of you with a full refund or exchange."
            ],
            'book_description': "",
            'product_description': '',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/512SEBYTT9L._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51-xk9GIKGL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41Jn5%2Bxc4oL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/61PZ4SE0qIL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/610oirnSUGL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41KcwKShDBL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/31jW36mmQJL._SS40_.jpg'
            ],
            'star': 4.5,
            'reviews': 105,
            'rank': 25654,
            'categories': u"Home & Kitchen>Home Décor>Slipcovers>Dining Chair Slipcovers;Home & Kitchen>Kitchen & Dining>Food Service Equipment & Supplies",
            'details': {
                "Package Dimensions": "6.5 x 4.1 x 2.6 inches",
                "Item Weight": "4.2 ounces",
                "Shipping Weight": "4.2 ounces",
                "Manufacturer": "uxcell",
                "ASIN": "B01LW7X0JJ",
                "Item model number": "US-SA-AJD-159579"
            }
        },
        'B07CL39Z8Q': {
            'title': 'Palarn Women Tops, Sexy O-Neck Flora Printed Sleeveless Vest Chiffon Tops T-Shirt Blouse',
            'author': ['Palarn'],
            'bylines': {},
            'feature_bullets': [
                'Cotton Blended',
                'Imported',
                'Casual print tank tops blouse makes you more lovely and vitality, show your personality wearing style',
                'Material:the soft high quality materials',
                'Ladies sleeveless vest blouse outside daily life sexy loose T-shirts',
                'Occasion: Casual,party,daily,etc.',
                'This sexy flora print lace back tank top is such a gorgeous look for spring and summer!'
            ],
            'book_description': "",
            'product_description': 'It is made by high quality and comfortable materials',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/51JFPnW7C7L._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51tk9aKEfGL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51ADMUIKozL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/511NOKZyNfL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51z21w0STEL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51Kr88zq2vL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51wkYMWv6zL._SR38,50_.jpg'
            ],
            'star': 0,
            'reviews': 0,
            'rank': 409707,
            'categories': "Clothing, Shoes & Jewelry>Women>Clothing>Tops, Tees & Blouses;Clothing, Shoes & Jewelry>Women>Shops",
            'details': {
                'Shipping Weight': '1.6 ounces',
                'ASIN': 'B07CLN88MV',
                'Date first listed on Amazon': 'March 28, 2018'
            }
        },
        'B07H57DNVV': {
            'title': 'Anthem Of The Peaceful Army',
            'author': ['Greta Van Fleet'],
            'bylines': {
                'Format': 'Audio CD'
            },
            'feature_bullets': [],
            'book_description': "",
            'product_description': '',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/51aXHugT30L._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51Ez5%2BghirL._SS40_.jpg'
            ],
            'star': 4.3,
            'reviews': 33,
            'rank': 2,
            'categories': "",
            'details': {
                'Audio CD': '(October 19, 2018)',
                'Original Release Date': 'October 19, 2018',
                'Number of Discs': '1',
                'Label': 'Lava Music',
                'ASIN': 'B07H57DNVV'
            }
        },
        'B00004YS4O': {
            'title': 'The Cars Live - Musikladen 1979',
            'author': ['Ric Ocasek', 'Ben Orr'],
            'bylines': {
                'Rated': 'NR',
                'Format': 'DVD'
            },
            'feature_bullets': [],
            'book_description': "",
            'product_description': '',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/41oaL7KbUzL._SX38_SY50_CR,0,0,38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51atWyKYatL._SX38_SY50_CR,0,0,38,50_.jpg'
            ],
            'star': 4.0,
            'reviews': 79,
            'rank': 119893,
            'categories': "CDs & Vinyl>Alternative Rock>New Wave & Post-Punk>New Wave;Movies & TV>DVD>Performing Arts;Movies & TV>DVD>Music Videos & Concerts",
            'details': {
                'Actors': 'Ric Ocasek,Ben Orr,Greg Hawkes,Elliot Easton,David Robinson',
                'Format': 'Color, Dolby, PAL',
                'Language': 'English (Dolby Digital 5.1), Unknown (Dolby Digital 5.1)',
                'Region': 'Region 1',
                'Aspect Ratio': '1.33:1',
                'Number of discs': '1',
                'Rated': 'Not Rated',
                'Studio': 'Rhino',
                'DVD Release Date': 'October 24, 2000',
                'Run Time': '93 minutes',
                'ASIN': 'B00004YS4O'
            }
        }
    }

@pytest.fixture(scope='session')
def ca_target_details():
    return {
        '0062796984': {
            'title': 'The Confidence Code for Girls: Taking Risks, Messing Up, and Becoming Your Amazingly Imperfect, Totally Powerful Self',
            'author': ['Katty Kay', 'Claire Shipman', 'JillEllyn Riley', 'Nan Lawson'],
            'bylines': {},
            'feature_bullets': [],
            'book_description': 'Girls can rule the world',
            'product_description': '',
            'images': ['https://images-na.ssl-images-amazon.com/images/I/51swWrRnF0L._AC_SX60_CR,0,0,60,60_.jpg', 'https://images-na.ssl-images-amazon.com/images/I/51jXn1jiPKL._AC_SX60_CR,0,0,60,60_.jpg'],
            'star': 4.4,
            'reviews': 8,
            'rank': 682,
            'categories': "Books>Children's Books>Growing Up & Facts of Life>Friendship, Social Skills & School Life>Self-Esteem & Self-Respect;Books>Children's Books>Growing Up & Facts of Life>Friendship, Social Skills & School Life>Girls & Women;Books>Children's Books>Growing Up & Facts of Life>Friendship, Social Skills & School Life>Emotions & Feelings",
            'details': {
                'Hardcover': '320 pages',
                'Publisher': 'HarperCollins (April 3 2018)',
                'Language': 'English',
                'ISBN-10': '0062796984',
                'ISBN-13': '978-0062796981',
                'Product Dimensions': '14 x 2.7 x 21 cm',
                'Shipping Weight': '748 g',
            }
        },
        '0131103628': {
            'title': 'C Programming Language (2nd Edition)',
            'author': ['Brian W. Kernighan', 'Dennis Ritchie'],
            'bylines': {},
            'feature_bullets': [],
            'book_description': "The authors present the complete guide to ANSI standard C language programming.",
            'product_description': '',
            'images': ['https://images-na.ssl-images-amazon.com/images/I/41gHB8KelXL._AC_SX60_CR,0,0,60,60_.jpg', 'https://images-na.ssl-images-amazon.com/images/I/41UqlrxbURL._AC_SX60_CR,0,0,60,60_.jpg', 'https://images-na.ssl-images-amazon.com/images/I/31ujUQ4UcXL._AC_SX60_CR,0,0,60,60_.jpg'],
            'star': 4.7,
            'reviews': 145,
            'rank': 23906,
            'categories': "Books>Computers & Technology>Programming>C>Language;Books>Computers & Technology>Programming>Languages & Tools>C;Books>Textbooks>Computer Science & Information Systems>Programming Languages",
            'details': {
                'Paperback': '288 pages',
                'Publisher': 'Prentice Hall; 2 edition (March 22 1988)',
                'Language': 'English',
                'ISBN-10': '0131103628',
                'ISBN-13': '978-0131103627',
                'Product Dimensions': '17.5 x 2.3 x 23.4 cm',
                'Shipping Weight': '567 g',
            }
        },
        '1439878676': {
            'title': 'Hydroponic Food Production: A Definitive Guidebook for the Advanced Home Gardener and the Commercial Hydroponic Grower, Seventh Edition',
            'author': ['Howard M. Resh'],
            'bylines': {},
            'feature_bullets': [],
            'book_description': "Hydroponic Food Production: A Definitive Guidebook for the Advanced Home Gardener and the Commercial Hydroponic Grower, Seventh Edition",
            'product_description': '',
            'images': ['https://images-na.ssl-images-amazon.com/images/I/51gOm0nTLXL._AC_SX60_CR,0,0,60,60_.jpg', 'https://images-na.ssl-images-amazon.com/images/I/51T-qNV9LkL._AC_SX60_CR,0,0,60,60_.jpg', 'https://images-na.ssl-images-amazon.com/images/I/41qkb49gfbL._AC_SX60_CR,0,0,60,60_.jpg'],
            'star': 4.6,
            'reviews': 5,
            'rank': 32007,
            'categories': "Books>Textbooks>Sciences>Biology & Life Sciences>Botany;Books>Textbooks>Sciences>Agriculture;Books>Professional & Technical>Professional Science>Biological Sciences>Botany",
            'details': {
                'Hardcover': '560 pages',
                'Publisher': 'CRC Press; 7 edition (Aug. 9 2012)',
                'Language': 'English',
                'ISBN-10': '9781439878675',
                'ISBN-13': '978-1439878675',
                'ASIN': '1439878676',
                'Product Dimensions': '18 x 3.3 x 25.4 cm',
                'Shipping Weight': '1.1 Kg',
            }
        },
        'B01GAWQSFW': {
            'title': 'Simple Leather Vintage Female Quartz Watch Wristwatch Black',
            'author': ['LinTimes'],
            'bylines': {},
            'feature_bullets': [
                'Vintage bracelet wrist watch for women or ladies.100% brand new with fabulous appearance.',
                'Thickness:5mm, Dial diameter:23mm,Buckle and case material:Stainless Steel',
                'Unique design;Naturally beautiful and durable. Very Lightweight and comfortable on the wrist.',
                'Suits for ladies girls, family members, holiday gifts, festival gifts, other etc.',
                'Nice present for yourself or your friends.'
            ],
            'book_description': "",
            'product_description': 'Stylish and high quality Fashion Watch',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/41ZKssAM9zL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41d5dTDS7SL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41sKncb2bjL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/513k1k3BhxL._SR38,50_.jpg',
            ],
            'star': 0,
            'reviews': 0,
            'rank': 44838,
            'categories': "Watches>Women's Watches>Wrist Watches",
            'details': {
                'Shipping Weight': '22.7 g',
                'Item model number': '4331797957',
                'ASIN': 'B01GAWQSFW',
                'Date first available at Amazon.ca': 'May 29 2016',
            }
        },
        'B01LW7X0JJ': {
            'title': u'uxcell® Dining Chair Cover,Stretch Bar Stool Slipcover Kitchen Pattern Chair Protector Spandex Short Chair Seat Cover for Home Decorative/Dining Room/Party/Wedding (Medium,White + Black)',
            'author': ['uxcell'],
            'bylines': {},
            'feature_bullets': [
                u'√High Stretchable:Spandex chair covers made of elastic fabric,suitable for medium&large chair,it can protect your furniture from spills, stains, wear and tear.',
                u'√Wrinkle Resistant: Cotton chair cover is fadeless and pilling resistance for long-lasting durability.Waterproof chair slipcovers can secure fit with sewn-in plastic fabric and cover your chairs quickly, bring a new face to your high back chair.',
                u'√Washable:Do not bleach, tumble dry low, do not Ironing. Washable chair cover is perfect for armless chair,wood chair,tall back chair,computer chair,office chair and counter height chair.',
                u'√Applicable Occasions:Dining chair covers are stylish and elegant design, it is perfect for home decor kitchen, dining room,bedroom, living room, office or meeting room, hotel, wedding banquet, celebration and ceremony.',
                u'√Size: Chair-back height 16.5 Inch-21.3 Inch (42-54 cm) and chair-back width 15 Inch-17.7 Inch (38-45 cm). Chair seat width and length 15 Inch-17.7 Inch (38-45 cm)and thickness 1.5 Inch-4 Inch (4-10 cm).',
            ],
            'book_description': "",
            'product_description': 'Redecorate your dining room in style with this Stretch Dining Room Chair Cover',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/41rnEgYIDSL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51-xk9GIKGL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41Jn5%2Bxc4oL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51FvEWyRUaL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51BP0wG5FIL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/418o0yPRCpL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/31s5ApiMRFL._SS40_.jpg',
            ],
            'star': 4.5,
            'reviews': 111,
            'rank': 0,
            'categories': u"Home>Home Décor>Slipcovers>Dining Chair Slipcovers;Home>Home Textiles",
            'details': {
                'Product Dimensions': '10 x 8 x 3 cm',
                'Shipping Weight': '118 g',
                'Item model number': 'US-SA-AJD-159579',
                'ASIN': 'B01LW7X0JJ',
                'Date first available at Amazon.ca': 'Sept. 9 2016',
            }
        },
        'B07CL39Z8Q': {
            'title': 'Palarn Women Tops, Sexy O-Neck Flora Printed Sleeveless Vest Chiffon Tops T-Shirt Blouse',
            'author': ['Palarn'],
            'bylines': {},
            'feature_bullets': [
                'Cotton Blended',
                'Casual print tank tops blouse makes you more lovely and vitality, show your personality wearing style',
                'Material:the soft high quality materials',
                'Ladies sleeveless vest blouse outside daily life sexy loose T-shirts',
                'Occasion: Casual,party,daily,etc.',
                'This sexy flora print lace back tank top is such a gorgeous look for spring and summer!',
            ],
            'book_description': "",
            'product_description': 'It is made by high quality and comfortable materials',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/51JFPnW7C7L._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51tk9aKEfGL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51ADMUIKozL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/511NOKZyNfL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51z21w0STEL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51Kr88zq2vL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51wkYMWv6zL._SR38,50_.jpg',
            ],
            'star': 0,
            'reviews': 0,
            'rank': 0,
            'categories': "",
            'details': {
                'Item Weight': '36.3 g',
                'Shipping Weight': '45.4 g',
                'ASIN': 'B07CL39Z8Q',
                'Date first available at Amazon.ca': 'April 25 2018',
            }
        },
        'B07H57DNVV': {
            'title': 'Anthem Of The Peaceful Army',
            'author': ['Greta Van Fleet'],
            'bylines': {
                'Format': 'Audio CD'
            },
            'feature_bullets': [],
            'book_description': "",
            'product_description': '',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/51aXHugT30L._SX38_SY50_CR,0,0,38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51Ez5%2BghirL._SX38_SY50_CR,0,0,38,50_.jpg'
            ],
            'star': 4.2,
            'reviews': 68,
            'rank': 31,
            'categories': "",
            'details': {
                'Audio CD': '(Oct. 19 2018)',
                'Number of Discs': '1',
                'Format': 'Original recording',
                'Label': 'Universal Music',
                'ASIN': 'B07H57DNVV',
                'Other Editions': 'Audio CD | LP Record',
            }
        },
        'B00004YS4O': {
            'title': 'The Cars Live Musikladen 1979 (International Release)',
            'author': [],
            'bylines': {
                'Rated': 'NR (Not Rated)',
                'Format': 'DVD'
            },
            'feature_bullets': [],
            'book_description': "",
            'product_description': '',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/41oaL7KbUzL._SX38_SY50_CR,0,0,38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51atWyKYatL._SX38_SY50_CR,0,0,38,50_.jpg'
            ],
            'star': 3.1,
            'reviews': 25,
            'rank': 100107,
            'categories': "Movies & TV Shows>Performing Arts;Music>Indie & Alternative>New Wave & Post-Punk>New Wave;Movies & TV Shows>Music Video & Concert",
            'details': {
                'Format': 'Color, Dolby, DVD-Video, NTSC',
                'Language': 'English',
                'Region': 'Region 1',
                'Aspect Ratio': '1.33:1',
                'Number of discs': '1',
                'MPAA Rating': '',
                'Studio': 'Warner',
                'Release Date': 'Sept. 17 2003',
                'Run Time': '93 minutes',
                'ASIN': 'B00004YS4O',
            }
        }
    }

@pytest.fixture(scope='session')
def uk_target_details():
    return {
        '0062796984': {
            'title': 'The Confidence Code for Girls: Taking Risks, Messing Up, and Becoming Your Amazingly Imperfect, Totally Powerful Self',
            'author': ['Katty Kay', 'Claire Shipman', 'JillEllyn Riley', 'Nan Lawson'],
            'bylines': {},
            'feature_bullets': [],
            'book_description': 'Girls can rule the world',
            'product_description': '',
            'images': ['https://images-na.ssl-images-amazon.com/images/I/51swWrRnF0L._AC_SX60_CR,0,0,60,60_.jpg', 'https://images-na.ssl-images-amazon.com/images/I/51jXn1jiPKL._AC_SX60_CR,0,0,60,60_.jpg'],
            'star': 5.0,
            'reviews': 17,
            'rank': 7201,
            'categories': "Children's Books on Girls & Women;Children's Books on Emotions & Feelings;Children's Books on Self-Esteem & Self-Respect",
            'details': {
                'Hardcover': '320 pages',
                'Age Range': '8 - 12 years',
                'Publisher': 'HarperCollins (3 May 2018)',
                'Language': 'English',
                'ISBN-10': '0062796984',
                'ISBN-13': '978-0062796981',
                'Product Dimensions': '14 x 2.7 x 21 cm'
            }
        },
        '0131103628': {
            'title': 'The  C Programming Language (2nd Edition)',
            'author': ['Brian W. Kernighan', 'Dennis Ritchie'],
            'bylines': {},
            'feature_bullets': [],
            'book_description': 'This second editon describes C as defined by the ANSI standard.',
            'product_description': '',
            'images': ['https://images-na.ssl-images-amazon.com/images/I/51TGEPRTDNL._AC_SX60_CR,0,0,60,60_.jpg'],
            'star': 4.5,
            'reviews': 131,
            'rank': 8557,
            'categories': "Programming Languages & Tools;Amazon Online Shopping;Programming Languages",
            'details': {
                'Paperback': '288 pages',
                'Publisher': 'Prentice Hall; 2nd edition (22 Mar. 1988)',
                'Language': 'English',
                'ISBN-10': '0131103628',
                'ISBN-13': '978-0131103627',
                'Product Dimensions': '17.5 x 2.3 x 23.4 cm'
            }
        },
        '1439878676': {
            'title': 'Hydroponic Food Production: A Definitive Guidebook for the Advanced Home Gardener and the Commercial Hydroponic Grower, Seventh Edition',
            'author': ['Howard M. Resh'],
            'bylines': {},
            'feature_bullets': [],
            'book_description': 'Hydroponic Food Production: A Definitive Guidebook for the Advanced Home Gardener',
            'product_description': '',
            'images': ['https://images-na.ssl-images-amazon.com/images/I/51gOm0nTLXL._AC_SX60_CR,0,0,60,60_.jpg', 'https://images-na.ssl-images-amazon.com/images/I/51T-qNV9LkL._AC_SX60_CR,0,0,60,60_.jpg', 'https://images-na.ssl-images-amazon.com/images/I/41qkb49gfbL._AC_SX60_CR,0,0,60,60_.jpg'],
            'star': 3.1,
            'reviews': 3,
            'rank': 640548,
            'categories': "Hydroponics (Books);Home Farming;Gardening Soil Science",
            'details': {
                'Hardcover': '560 pages',
                'Publisher': 'CRC Press; 7 edition (8 Sept. 2012)',
                'Language': 'English',
                'ISBN-10': '9781439878675',
                'ISBN-13': '978-1439878675',
                'ASIN': '1439878676',
                'Product Dimensions': '18 x 3.3 x 25.4 cm'
            }
        },
        'B01GAWQSFW': {
            'title': 'Simple Leather Vintage Female Quartz Watch Wristwatch Black',
            'author': ['Lintimes'],
            'bylines': {},
            'feature_bullets': [
                'Vintage bracelet wrist watch for women or ladies.100% brand new with fabulous appearance.',
                'Thickness:5mm, Dial diameter:23mm,Buckle and case material:Stainless Steel',
                'Unique design;Naturally beautiful and durable. Very Lightweight and comfortable on the wrist.',
                'Suits for ladies girls, family members, holiday gifts, festival gifts, other etc.',
                'Nice present for yourself or your friends.'
            ],
            'book_description': '',
            'product_description': 'Stylish and high quality Fashion Watch',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/41ZKssAM9zL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41d5dTDS7SL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41sKncb2bjL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/513k1k3BhxL._SR38,50_.jpg'
            ],
            'star': 0,
            'reviews': 0,
            'rank': 0,
            'categories': "",
            'details': {
                'Boxed-product Weight': '22.7 g',
                'Delivery Destinations': 'Visit the  Help page to see where this item can be delivered.Find out more about our',
                'Item model number': '4331797957',
                'ASIN': 'B01GAWQSFW',
                'Date first available at Amazon.co.uk': '29 May 2016'
            }
        },
        'B01LW7X0JJ': {
            'title': 'Sourcingmap Stretch Washable Short Dining Room Chair Protector Cover Slipcovers Home Decor White + Black',
            'author': ['Sourcingmap'],
            'bylines': {},
            'feature_bullets': ['Global Store items have separate terms, are sold from abroad, and may differ from the UK version, including fit, age ratings, and labelling.'],
            'book_description': '',
            'product_description': 'Refresh your dining room in style with this Stretch Dining Room Chair Cover',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/512SEBYTT9L._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41BJeSG9EfL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/610oirnSUGL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51t0ktYuRiL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/61HXuyOASZL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41uqy89XazL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/31jW36mmQJL._SS40_.jpg'
            ],
            'star': 4.8,
            'reviews': 11,
            'rank': 330931,
            'categories': "Dining Chair Slipcovers",
            'details': {
                'Brand': 'Sourcingmap',
                'Model Number': 'a16082300ux1011',
                'Colour': 'White + Black',
                'Item Weight': '118 g',
                'Product Dimensions': '10 x 8 x 3 cm',
                'Material': 'Spandex',
                'ASIN': 'B01LW7X0JJ',
                'Shipping Weight': '118 g',
                'Delivery Destinations': 'Visit the',
                'Date First Available': '24 May 2017'
            }
        },
        'B00004YS4O': {
            'title': 'The Cars: Musikladen 1979 [2007]',
            'author': [],
            'bylines': {
                'Rated': 'Exempt',
                'Format': 'DVD'
            },
            'feature_bullets': [],
            'book_description': '',
            'product_description': '',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/41oaL7KbUzL._SX38_SY50_CR,0,0,38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51atWyKYatL._SX38_SY50_CR,0,0,38,50_.jpg'
            ],
            'star': 3.0,
            'reviews': 1,
            'rank': 34557,
            'categories': "Music Video & Concert",
            'details': {
                'Format': 'Colour, Dolby, DVD-Video, NTSC',
                'Language': 'English',
                'Region': 'Region 2',
                'Aspect Ratio': '4:3 - 1.33:1',
                'Number of discs': '1',
                'Classification': 'Exempt',
                'Studio': 'Wmv',
                'DVD Release Date': '23 Jun. 2003',
                'Run Time': '93 minutes',
                'ASIN': 'B00004YS4O'
            }
        },
        'B07CL39Z8Q': {
            'title': 'Palarn Women Tops, Sexy O-Neck Flora Printed Sleeveless Vest Chiffon Tops T-Shirt Blouse',
            'author': ['Palarn'],
            'bylines': {},
            'feature_bullets': [
                'Casual print tank tops blouse makes you more lovely and vitality, show your personality wearing style',
                'Material:the soft high quality materials',
                'Chiffon',
                'Regular',
                'Sleeveless',
                'Ladies sleeveless vest blouse outside daily life sexy loose T-shirts',
                'Occasion: Casual,party,daily,etc.',
                'This sexy flora print lace back tank top is such a gorgeous look for spring and summer!'
            ],
            'book_description': '',
            'product_description': 'It is made by high quality and comfortable materials',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/51JFPnW7C7L._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51tk9aKEfGL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51ADMUIKozL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/511NOKZyNfL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51z21w0STEL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51Kr88zq2vL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51wkYMWv6zL._SR38,50_.jpg'
            ],
            'star': 0,
            'reviews': 0,
            'rank': 0,
            'categories': "",
            'details': {
                'Boxed-product Weight': '45.4 g',
                'Delivery Destinations': 'Visit the  Help page to see where this item can be delivered.Find out more about our',
                'ASIN': 'B07CL39Z8Q',
                'Date first available at Amazon.co.uk': '28 Mar. 2018'
            }
        },
        'B07H57DNVV': {
            'title': 'Anthem Of The Peaceful Army',
            'author': ['Greta Van Fleet'],
            'bylines': {'Format': 'Audio CD'},
            'feature_bullets': [],
            'book_description': '',
            'product_description': u'Greta Van Fleet - Jake Kiszka/guitars, Sam Kiszka/bass & keys, Josh Kiszka/vocals, and Danny Wagner/drums - is very proud to announce the upcoming release of the band’s debut album',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/51aXHugT30L._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51Ez5%2BghirL._SS40_.jpg'
            ],
            'star': 4.6,
            'reviews': 136,
            'rank': 452,
            'categories': "Alternative Rock",
            'details': {
                'Audio CD': '(19 Oct. 2018)',
                'Number of Discs': '1',
                'Label': 'EMI',
                'ASIN': 'B07H57DNVV',
                'Other Editions': 'Audio CD | Vinyl | MP3 Download'
            }
        },
    }

@pytest.fixture(scope='session')
def de_target_details():
    return {
        '0062796984': {
            'title': 'The Confidence Code for Girls: Taking Risks, Messing Up, and Becoming Your Amazingly Imperfect, Totally Powerful Self',
            'author': ['Katty Kay', 'Claire Shipman', 'JillEllyn Riley', 'Nan Lawson'],
            'bylines': {},
            'feature_bullets': [],
            'book_description': 'Girls can rule the world',
            'product_description': '',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/51swWrRnF0L._AC_SX60_CR,0,0,60,60_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51jXn1jiPKL._AC_SX60_CR,0,0,60,60_.jpg'
            ],
            'star': 4.5,
            'reviews': 2,
            'rank': 52871,
            'categories': u"Kinderbücher zu Selbstbewusstsein;Kinderbücher zu Emotionen & Gefühlen;Soziale Themen für Kinder",
            'details': {
                'Gebundene Ausgabe': '320 Seiten',
                'Verlag': 'HarperCollins (3. April 2018)',
                'Sprache': 'Englisch',
                'ISBN-10': '0062796984',
                'ISBN-13': '978-0062796981',
                'Vom Hersteller empfohlenes Alter': '8 - 12 Jahre',
                u'Größe und/oder Gewicht': '14 x 2,7 x 21 cm'
            }
        },
        '0131103628': {
            'title': 'The C Programming Language. (Prentice Hall Software)',
            'author': ['Brian W. Kernighan', 'Dennis Ritchie'],
            'bylines': {},
            'feature_bullets': [],
            'book_description': 'Introduces the features of the C programming language',
            'product_description': '',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/41gHB8KelXL._AC_SX60_CR,0,0,60,60_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41UqlrxbURL._AC_SX60_CR,0,0,60,60_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/31ujUQ4UcXL._AC_SX60_CR,0,0,60,60_.jpg'
            ],
            'star': 4.2,
            'reviews': 56,
            'rank': 13222,
            'categories': "C",
            'details': {
                'Taschenbuch': '274 Seiten',
                'Verlag': 'Markt+Technik Verlag; Auflage: 2nd ed (7. Februar 2000)',
                'Sprache': 'Englisch',
                'ISBN-10': '0131103628',
                'ISBN-13': '978-0131103627',
                u'Größe und/oder Gewicht': '17,5 x 2,3 x 23,4 cm'
            }
        },
        '1439878676': {
            'title': 'Hydroponic Food Production: A Definitive Guidebook for the Advanced Home Gardener and the Commercial Hydroponic Grower, Seventh Edition',
            'author': ['Howard M. Resh'],
            'bylines': {},
            'feature_bullets': [],
            'book_description': 'Hydroponic Food Production: A Definitive Guidebook for the Advanced Home Gardener and the Commercial Hydroponic Grower',
            'product_description': '',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/51gOm0nTLXL._AC_SX60_CR,0,0,60,60_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51T-qNV9LkL._AC_SX60_CR,0,0,60,60_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41qkb49gfbL._AC_SX60_CR,0,0,60,60_.jpg'
            ],
            'star': 0,
            'reviews': 0,
            'rank': 190823,
            'categories': u"Botanik (Fremdsprachige Bücher);Fachbücher Agrarwissenschaften;Outdoor, Umwelt & Natur",
            'details': {
                'Gebundene Ausgabe': '560 Seiten',
                'Verlag': 'Taylor & Francis Inc; Auflage: 7 New edition (8. September 2012)',
                'Sprache': 'Englisch',
                'ISBN-10': '9781439878675',
                'ISBN-13': '978-1439878675',
                'ASIN': '1439878676',
                u'Größe und/oder Gewicht': '18 x 3,3 x 25,4 cm'
            }
        },
        'B01GAWQSFW': {
            'title': 'Einfache Leder Vintage weiblich Quarzuhr Armbanduhr Schwarz',
            'author': ['Lintimes'],
            'bylines': {},
            'feature_bullets': [
                u'Vintage Armband Armbanduhr für Frauen oder Damen.100% Marke neue mit fabelhaft aussehen.',
                u'Dicke: 5 mm, Durchmesser Zifferblatt: 23 mm, Schnalle und Fall Material: Edelstahl',
                u'Einzigartiges Design; natürlich schön und stabil. Sehr leicht und bequem am Handgelenk.',
                u'Passend für für Damen Mädchen, Familie Mitglieder, Festival, Urlaub Geschenk, andere etc.',
                u'Nettes Geschenk für sich selbst oder Ihre Freunde.'
            ],
            'book_description': '',
            'product_description': '<br/> Beschreibung:<br/>Stilvolle und hochwertige Fashion Armbanduhr<br/> - Uhrwerk',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/41ZKssAM9zL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41d5dTDS7SL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41sKncb2bjL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/513k1k3BhxL._SR38,50_.jpg'
            ],
            'star': 0,
            'reviews': 0,
            'rank': 0,
            'categories': "",
            'details': {
                'Produktgewicht inkl. Verpackung': '22,7 g',
                'Modellnummer': '4331797957',
                'ASIN': 'B01GAWQSFW',
                'Im Angebot von Amazon.de seit': '25. August 2016'
            }
        },
        'B01LW7X0JJ': {
            'title': u'Abnehmbarer dehnbar Gummiband Schutzhüllen kurze Esszimmer Stuhl Sitzbezüge de',
            'author': ['sourcing map'],
            'bylines': {},
            'feature_bullets': [
                u'Weich, bequem und knitterarm, kein Bügeln erforderlich;',
                u'Geeignet für Größe: Stuhl Rückhöhe: 45 cm - 60cm/17 bis 23 Zoll; Stuhl Breite des Rückens: 35 cm - 48cm/13 bis 19 Zoll; Sitzgröße: 38 cm - 46cm/15 bis 18 Zoll;',
                u'100 % brandneue, leicht zu reinigen und waschen, maschinenwaschbar;',
                u'Dehnbaren Material, dehnen, wiederstellen schnell, sicherer Sitz mit eingenähter elastische Saum;',
                u'Für Hotel, Hochzeitsbankett, Abendessen, Besprechung, Feier, Zeremonie, Familie Esszimmer Dekoration verwendet werden.'
            ],
            'book_description': '',
            'product_description': '',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/512SEBYTT9L._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41BJeSG9EfL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/610oirnSUGL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51t0ktYuRiL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/61HXuyOASZL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41uqy89XazL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/31jW36mmQJL._SS40_.jpg'
            ],
            'star': 0,
            'reviews': 0,
            'rank': 1234207,
            'categories': "Hussen",
            'details': {
                # 'Farbe': u'WeiÃŸ + Schwarz',
                u'Größe und/oder Gewicht': '10 x 8 x 3 cm ; 118 g',
                'Ausgangsmaterial': 'Spandex',
                u'Größe': 'Medium',
                'Versandgewicht': '118 Gramm',
                'Modellnummer': 'US-SA-AJD-159579',
                'ASIN': 'B01LW7X0JJ',
                'Produktgewicht inkl. Verpackung': '118 g',
                'Modellnummer': 'US-SA-AJD-159579',
                'Im Angebot von Amazon.de seit': '1. Oktober 2016'
            }
        },
        'B00004YS4O': {
            'title': 'The Cars - Live',
            'author': ['The Cars'],
            'bylines': {
                'Alterseinstufung': u'Freigegeben ohne Altersbeschränkung',
                'Format': 'DVD'
            },
            'feature_bullets': [],
            'book_description': '',
            'product_description': 'Shot live at Radio Bremen studios, Germany, and braodcast June 7, 1979',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/41oaL7KbUzL._SX38_SY50_CR,0,0,38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51atWyKYatL._SX38_SY50_CR,0,0,38,50_.jpg'
            ],
            'star': 1.0,
            'reviews': 1,
            'rank': 213549,
            'categories': "Musik (DVD & Blu-ray)",
            'details': {
                # 'Darsteller': 'The Cars',
                'Format': 'Dolby, NTSC, Surround-Sound',
                'Sprache': 'Englisch (Dolby Digital 5.1), Unbekannt (Dolby Digital 5.1)',
                'Region': 'Alle Regionen',
                'Bildseitenformat': '4:3 - 1.33:1',
                'Anzahl Disks': '1',
                'FSK': u'Freigegeben ohne Altersbeschränkung',
                'Studio': 'Warner Music Group Germany',
                'Erscheinungstermin': '2. Juni 2003',
                'Produktionsjahr': '1978',
                'Spieldauer': '93 Minuten',
                'ASIN': 'B00004YS4O'
            }
        },
        'B07H57DNVV': {
            'title': 'Anthem of the Peaceful Army',
            'author': ['Greta Van Fleet'],
            'bylines': {'Format': 'Audio CD'},
            'feature_bullets': [],
            'book_description': '',
            'product_description': u'Endlich ist es offiziell: Nach zwei bombastischen EPs erscheint das Debütalbum Anthem Of The Peaceful Army der Rock-n-Roll-Sensation Greta Van Fleet.',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/51aXHugT30L._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51Ez5%2BghirL._SS40_.jpg'
            ],
            'star': 4.6,
            'reviews': 134,
            'rank': 109,
            'categories': "Rock (Musik-CDs & Vinyl)",
            'details': {
                'Audio CD': '(19. Oktober 2018)',
                'Erscheinungsdatum': '19. Oktober 2018',
                u'Anzahl Disks/Tonträger': '1',
                'Label': 'Republic (Universal Music)',
                'ASIN': 'B07H57DNVV',
                'Weitere Ausgaben': 'Audio CD | Vinyl | MP3-Download'
            }
        },
    }

@pytest.fixture(scope='session')
def fr_target_details():
    return {
        '0062796984': {
            'title': 'The Confidence Code for Girls: Taking Risks, Messing Up, and Becoming Your Amazingly Imperfect, Totally Powerful Self',
            'author': ['Katty Kay', 'Claire Shipman', 'JillEllyn Riley', 'Nan Lawson'],
            'bylines': {},
            'feature_bullets': [],
            'book_description': u'Girls can rule the world—all they need is confidence.',
            'product_description': '',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/51swWrRnF0L._AC_SX60_CR,0,0,60,60_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51jXn1jiPKL._AC_SX60_CR,0,0,60,60_.jpg'
            ],
            'star': 3.0,
            'reviews': 1,
            'rank': 25472,
            'categories': u"Children's Self-Esteem Books (Livres anglais et étrangers);Children's Emotions & Feelings Books (Livres anglais et étrangers);Children's Social Issues (Livres anglais et étrangers)",
            'details': {
                u'Relié': '320 pages',
                'Editeur': 'HarperCollins (3 avril 2018)',
                'Langue': 'Anglais',
                'ISBN-10': '0062796984',
                'ISBN-13': '978-0062796981',
                'Dimensions du produit': '14 x 2,7 x 21 cm'
            }
        },
        '0131103628': {
            'title': 'The C Programming Language',
            'author': ['Brian W. Kernighan', 'Dennis Ritchie'],
            'bylines': {},
            'feature_bullets': [],
            'book_description': 'This second editon describes C as defined by the ANSI standard.',
            'product_description': '',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/41gHB8KelXL._AC_SX60_CR,0,0,60,60_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41UqlrxbURL._AC_SX60_CR,0,0,60,60_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/31ujUQ4UcXL._AC_SX60_CR,0,0,60,60_.jpg'
            ],
            'star': 4.0,
            'reviews': 7,
            'rank': 3421,
            'categories': u"Computer Programming Language & Tool (Livres anglais et étrangers)",
            'details': {
                u'Broché': '288 pages',
                'Editeur': u'Prentice Hall;  2 (22 mars 1988)',
                'Langue': 'Anglais',
                'ISBN-10': '0131103628',
                'ISBN-13': '978-0131103627',
                'Dimensions du produit': '17,5 x 2,3 x 23,4 cm'
            }
        },
        '1439878676': {
            'title': 'Hydroponic Food Production: A Definitive Guidebook for the Advanced Home Gardener and the Commercial Hydroponic Grower, Seventh Edition',
            'author': ['Howard M. Resh'],
            'bylines': {},
            'feature_bullets': [],
            'book_description': 'Hydroponic Food Production: A Definitive Guidebook for the Advanced Home Gardener and the Commercial Hydroponic Grower',
            'product_description': '',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/51gOm0nTLXL._AC_SX60_CR,0,0,60,60_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51T-qNV9LkL._AC_SX60_CR,0,0,60,60_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41qkb49gfbL._AC_SX60_CR,0,0,60,60_.jpg'
            ],
            'star': 5.0,
            'reviews': 1,
            'rank': 124334,
            'categories': u"Botany (Livres anglais et étrangers);Agricultural Sciences (Livres anglais et étrangers)",
            'details': {
                u'Relié': '560 pages',
                'Editeur': u'CRC Press;  7 (8 septembre 2012)',
                'Langue': 'Anglais',
                'ISBN-10': '9781439878675',
                'ISBN-13': '978-1439878675',
                'ASIN': '1439878676',
                'Dimensions du produit': '18 x 3,3 x 25,4 cm'
            }
        },
        'B01GAWQSFW': {
            'title': u'Simple Cuir Vintage Femelle Montre à Quartz Montre-Bracelet Noir',
            'author': ['Lintimes'],
            'bylines': {},
            'feature_bullets': [
                'Vintage bracelet montre de poignet pour femme ou femme.100% neuf avec aspect fabuleux.',
                u'Épaisseur :, diamètre du cadran :, boucle et matériau du boîtier : acier inoxydable',
                u'Design unique ; naturellement beau et durable. Très léger et confortable sur le poignet.',
                u"Convient pour les femmes filles, membres de la famille, des cadeaux de vacances, festival cadeaux, d'autres, etc.",
                u'Joli cadeau pour vous-même ou vos amis.'
            ],
            'book_description': '',
            'product_description': u'<br/> Description :<br/>Design élégant et de haute qualité fashion montre<br/> Mouvement',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/41ZKssAM9zL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41d5dTDS7SL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41sKncb2bjL._SR38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/513k1k3BhxL._SR38,50_.jpg'
            ],
            'star': 0,
            'reviews': 0,
            'rank': 0,
            'categories': "",
            'details': {
                u"Numéro du modèle de l'article": '4331797957',
                'ASIN': 'B01GAWQSFW',
                'Date de mise en ligne sur Amazon.fr': u'25 août 2016'
            }
        },
        'B01LW7X0JJ': {
            'title': u'sourcingmap® Housses chaise housses amovibles Étendue Court Housse de siège Noir + Blanc',
            'author': ['Sourcingmap'],
            'bylines': {},
            'feature_bullets': [
                u'Doux et confortable, infroissable, aucun repassage nécessaire ;',
                u'Pour chaise Dimensions : Hauteur du dossier : 45 cm – 60 cm/17 à 58,4 cm ; Largeur : 35 cm – 48 cm/13 à 48,3 cm ; Longueur du siège : 38 cm – 46 cm/15 à 45,7 cm ;',
                u'100% neuf, facile à nettoyer et laver, lavable en machine,',
                u'Matière élastique, qui retrouve rapidement, confortable élastique avec ourlet cousu ;',
                u'Peut être utilisé pour hôtel, mariage, banquet, décoration, fête, cérémonie, la salle à manger, etc.'
            ],
            'book_description': '',
            'product_description': '',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/512SEBYTT9L._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41BJeSG9EfL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/610oirnSUGL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51t0ktYuRiL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/61HXuyOASZL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/41uqy89XazL._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/31jW36mmQJL._SS40_.jpg'
            ],
            'star': 0,
            'reviews': 0,
            'rank': 1892338,
            'categories': u"Housses de chaise de salle à manger",
            'details': {
                'Dimensions du produit': '10 x 8 x 3 cm',
                'Piles requises': 'Non',
                'ASIN': 'B01LW7X0JJ',
                u"Numéro du modèle de l'article": 'US-SA-AJD-159579',
                'Date de mise en ligne sur Amazon.fr': '30 septembre 2016'
            }
        },
        'B00004YS4O': {
            'title': 'The Cars : Live On Musikladen 1979',
            'author': ['The Cars'],
            'bylines': {
                u'Classé': 'Tous publics',
                'Format': 'DVD'
            },
            'feature_bullets': [],
            'book_description': '',
            'product_description': u'Concert enregistré à Musikladen en 1979',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/41oaL7KbUzL._SX38_SY50_CR,0,0,38,50_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51atWyKYatL._SX38_SY50_CR,0,0,38,50_.jpg'
            ],
            'star': 1.3,
            'reviews': 3,
            'rank': 177226,
            'categories': "Musique (DVD & Blu-ray)",
            'details': {
                'Format': u'DVD-Vidéo, Plein écran, NTSC',
                'Audio': u'Anglais (Dolby Digital 5.1), Inconnu (Dolby Digital 5.1)',
                u'Région': u"Région 2 (Ce DVD ne pourra probablement pas être visualisé en dehors de l'Europe. Plus d'informations sur .).",
                'Rapport de forme': '1.33:1',
                'Nombre de disques': '1',
                'Studio': 'Warner Vision France',
                'Date de sortie du DVD': u'26 décembre 2005',
                u'Durée': '93 minutes',
                'ASIN': 'B00004YS4O'
            }
        },
        'B07H57DNVV': {
            'title': 'Anthem of the Peaceful Army',
            'author': ['Greta Van Fleet', 'Samuel Francis Kiszka', 'Joshua Michael Kiszka', 'Jacob Thomas Kiszka', 'Daniel Robert Wagner', 'Marlon Young', 'Herschel Boone', 'Al Sutton'],
            'bylines': {'Format': 'CD'},
            'feature_bullets': [],
            'book_description': '',
            'product_description': '',
            'images': [
                'https://images-na.ssl-images-amazon.com/images/I/51aXHugT30L._SS40_.jpg',
                'https://images-na.ssl-images-amazon.com/images/I/51Ez5%2BghirL._SS40_.jpg'
            ],
            'star': 4.3,
            'reviews': 34,
            'rank': 167,
            'categories': "Pop Rock",
            'details': {
                'CD': '(19 octobre 2018)',
                'Nombre de disques': '1',
                'Label': 'Republic',
                'ASIN': 'B07H57DNVV',
                'Autres versions': u'CD | Album vinyle | Téléchargement MP3'
            }
        },
    }

# @pytest.fixture(scope='session')
# def it_target_details():
#     return {
#         '0062796984': {
#             'title': '',
#             'author': [],
#             'bylines': {},
#             'feature_bullets': [],
#             'book_description': '',
#             'product_description': '',
#             'images': [],
#             'star': ,
#             'reviews': ,
#             'rank': ,
#             'categories': "",
#             'details': {}
#         },
#         '': {
#             'title': '',
#             'author': [],
#             'bylines': {},
#             'feature_bullets': [],
#             'book_description': '',
#             'product_description': '',
#             'images': [],
#             'star': ,
#             'reviews': ,
#             'rank': ,
#             'categories': "",
#             'details': {}
#         },
#         '': {
#             'title': '',
#             'author': [],
#             'bylines': {},
#             'feature_bullets': [],
#             'book_description': '',
#             'product_description': '',
#             'images': [],
#             'star': ,
#             'reviews': ,
#             'rank': ,
#             'categories': "",
#             'details': {}
#         },
#         '': {
#             'title': '',
#             'author': [],
#             'bylines': {},
#             'feature_bullets': [],
#             'book_description': '',
#             'product_description': '',
#             'images': [],
#             'star': ,
#             'reviews': ,
#             'rank': ,
#             'categories': "",
#             'details': {}
#         },
#         '': {
#             'title': '',
#             'author': [],
#             'bylines': {},
#             'feature_bullets': [],
#             'book_description': '',
#             'product_description': '',
#             'images': [],
#             'star': ,
#             'reviews': ,
#             'rank': ,
#             'categories': "",
#             'details': {}
#         },
#         '': {
#             'title': '',
#             'author': [],
#             'bylines': {},
#             'feature_bullets': [],
#             'book_description': '',
#             'product_description': '',
#             'images': [],
#             'star': ,
#             'reviews': ,
#             'rank': ,
#             'categories': "",
#             'details': {}
#         },
#         '': {
#             'title': '',
#             'author': [],
#             'bylines': {},
#             'feature_bullets': [],
#             'book_description': '',
#             'product_description': '',
#             'images': [],
#             'star': ,
#             'reviews': ,
#             'rank': ,
#             'categories': "",
#             'details': {}
#         },
#     }

# @pytest.fixture(scope='session')
# def es_target_details():
#     return {
#         '0062796984': {
#             'title': '',
#             'author': [],
#             'bylines': {},
#             'feature_bullets': [],
#             'book_description': '',
#             'product_description': '',
#             'images': [],
#             'star': ,
#             'reviews': ,
#             'rank': ,
#             'categories': "",
#             'details': {}
#         },
#         '': {
#             'title': '',
#             'author': [],
#             'bylines': {},
#             'feature_bullets': [],
#             'book_description': '',
#             'product_description': '',
#             'images': [],
#             'star': ,
#             'reviews': ,
#             'rank': ,
#             'categories': "",
#             'details': {}
#         },
#         '': {
#             'title': '',
#             'author': [],
#             'bylines': {},
#             'feature_bullets': [],
#             'book_description': '',
#             'product_description': '',
#             'images': [],
#             'star': ,
#             'reviews': ,
#             'rank': ,
#             'categories': "",
#             'details': {}
#         },
#         '': {
#             'title': '',
#             'author': [],
#             'bylines': {},
#             'feature_bullets': [],
#             'book_description': '',
#             'product_description': '',
#             'images': [],
#             'star': ,
#             'reviews': ,
#             'rank': ,
#             'categories': "",
#             'details': {}
#         },
#         '': {
#             'title': '',
#             'author': [],
#             'bylines': {},
#             'feature_bullets': [],
#             'book_description': '',
#             'product_description': '',
#             'images': [],
#             'star': ,
#             'reviews': ,
#             'rank': ,
#             'categories': "",
#             'details': {}
#         },
#         '': {
#             'title': '',
#             'author': [],
#             'bylines': {},
#             'feature_bullets': [],
#             'book_description': '',
#             'product_description': '',
#             'images': [],
#             'star': ,
#             'reviews': ,
#             'rank': ,
#             'categories': "",
#             'details': {}
#         },
#         '': {
#             'title': '',
#             'author': [],
#             'bylines': {},
#             'feature_bullets': [],
#             'book_description': '',
#             'product_description': '',
#             'images': [],
#             'star': ,
#             'reviews': ,
#             'rank': ,
#             'categories': "",
#             'details': {}
#         },
#     }
