# -*- coding: utf-8 -*-

# @Author: hyan15
# @Email: qwang16@olivetuniversity.edu

import os
import codecs

from amazon_page_parser.parsers import DetailParser

import six
import pytest

@pytest.fixture(scope='module')
def shared_context():
    base_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pages', 'ca')

    context = dict()

    page_path = os.path.join(base_path, '0062796984.html')
    context['0062796984'] = {
        'page_path': page_path,
        'detail': {
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
        }
    }

    with codecs.open(page_path, encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if six.PY2:
            c = unicode(c)
        context['0062796984']['parser'] = DetailParser(c)

    page_path = os.path.join(base_path, '0131103628.html')
    context['0131103628'] = {
        'page_path': page_path,
        'detail': {
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
        }
    }

    with codecs.open(page_path, encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if six.PY2:
            c = unicode(c)
        context['0131103628']['parser'] = DetailParser(c)

    page_path = os.path.join(base_path, '1439878676.html')
    context['1439878676'] = {
        'page_path': page_path,
        'detail': {
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
        }
    }

    with codecs.open(page_path, encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if six.PY2:
            c = unicode(c)
        context['1439878676']['parser'] = DetailParser(c)

    page_path = os.path.join(base_path, 'B01GAWQSFW.html')
    context['B01GAWQSFW'] = {
        'page_path': page_path,
        'detail': {
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
        }
    }

    with codecs.open(page_path, encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if six.PY2:
            c = unicode(c)
        context['B01GAWQSFW']['parser'] = DetailParser(c)

    page_path = os.path.join(base_path, 'B01LW7X0JJ.html')
    context['B01LW7X0JJ'] = {
        'page_path': page_path,
        'detail': {
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
        }
    }

    with codecs.open(page_path, encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if six.PY2:
            c = unicode(c)
        context['B01LW7X0JJ']['parser'] = DetailParser(c)

    page_path = os.path.join(base_path, 'B07CL39Z8Q.html')
    context['B07CL39Z8Q'] = {
        'page_path': page_path,
        'detail': {
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
        }
    }

    with codecs.open(page_path, encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if six.PY2:
            c = unicode(c)
        context['B07CL39Z8Q']['parser'] = DetailParser(c)

    page_path = os.path.join(base_path, 'B07H57DNVV.html')
    context['B07H57DNVV'] = {
        'page_path': page_path,
        'detail': {
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
        }
    }

    with codecs.open(page_path, encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if six.PY2:
            c = unicode(c)
        context['B07H57DNVV']['parser'] = DetailParser(c)

    page_path = os.path.join(base_path, 'B00004YS4O.html')
    context['B00004YS4O'] = {
        'page_path': page_path,
        'detail': {
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

    with codecs.open(page_path, encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if six.PY2:
            c = unicode(c)
        context['B00004YS4O']['parser'] = DetailParser(c)

    yield context

def test_parse_title(shared_context):
    for k, v in shared_context.items():
        title = v['parser'].parse_title()
        assert title == v['detail']['title']

def test_parse_author(shared_context):
    for k, v in shared_context.items():
        author = v['parser'].parse_author()
        assert set(author) == set(v['detail']['author'])

def test_parse_feature_bullets(shared_context):
    for k, v in shared_context.items():
        feature_bullets = v['parser'].parse_feature_bullets()
        assert set(feature_bullets) == set(v['detail']['feature_bullets'])

def test_parse_book_description(shared_context):
    for k, v in shared_context.items():
        book_description = v['parser'].parse_book_description()
        assert book_description.find(v['detail']['book_description']) != -1

def test_parse_product_description(shared_context):
    for k, v in shared_context.items():
        product_description = v['parser'].parse_product_description()
        assert product_description.find(v['detail']['product_description']) != -1

def test_parse_images(shared_context):
    for k, v in shared_context.items():
        images = v['parser'].parse_images()
        assert set(images) == set(v['detail']['images'])

def test_parse_star(shared_context):
    for k, v in shared_context.items():
        star = v['parser'].parse_star()
        assert star == v['detail']['star']

def test_parse_reviews(shared_context):
    for k, v in shared_context.items():
        reviews = v['parser'].parse_reviews()
        assert reviews == v['detail']['reviews']

def test_parse_rank(shared_context):
    for k, v in shared_context.items():
        rank = v['parser'].parse_rank()
        assert rank == v['detail']['rank']

def test_parse_categories(shared_context):
    for k, v in shared_context.items():
        categories = v['parser'].parse_categories()
        assert categories == v['detail']['categories']

def test_parse_details(shared_context):
    for k, v in shared_context.items():
        details = v['parser'].parse_details()
        for dk, dv in v['detail']['details'].items():
            assert details.get(dk, '') == dv

def test_parse_byline(shared_context):
    for k, v in shared_context.items():
        bylines = v['parser'].parse_bylines()
        for dk, dv in v['detail']['bylines'].items():
            assert bylines.get(dk, '') == dv
