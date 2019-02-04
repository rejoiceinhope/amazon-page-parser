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
    base_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'pages', 'us')

    context = dict()

    page_path = os.path.join(base_path, '0062796984.html')
    context['0062796984'] = {
        'page_path': page_path,
        'detail': {
            'title': 'The Confidence Code for Girls: Taking Risks, Messing Up, and Becoming Your Amazingly Imperfect, Totally Powerful Self',
            'author': ['Katty Kay', 'Claire Shipman', 'JillEllyn Riley', 'Nan Lawson'],
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
            'title': 'C Programming Language, 2nd Edition',
            'author': ['Brian W. Kernighan', 'Dennis M. Ritchie'],
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
            'title': 'uxcell Stretch Spandex Short Dining Chair Covers Slipcovers Parson Chair Covers White + Black',
            'author': ['uxcell'],
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
        }
    }

    with codecs.open(page_path, encoding='utf-8', errors='ignore') as f:
        c = f.read()
        if six.PY2:
            c = unicode(c)
        context['B07H57DNVV']['parser'] = DetailParser(c)

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
