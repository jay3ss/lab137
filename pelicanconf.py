from pathlib import Path

import bulrush


# theme settings
THEME = bulrush.PATH
JINJA_ENVIRONMENT = bulrush.ENVIRONMENT
JINJA_FILTERS = bulrush.FILTERS

LICENSE = "CC BY-SA 4.0"
PLUGIN_PATHS = [str(Path("pelican-plugins").resolve())]
PLUGINS = ['assets', "render_math", "sitemap"]

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'css/custom.css'},
}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


# site settings
AUTHOR = 'Jay Ess'
SITENAME = 'Lab137'
SITEURL = ''

STATIC_PATHS = ["css", "img"]

PATH = 'content'
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ["pages"]

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

ARTICLE_URL = 'articles/{slug}/'
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'categories/{slug}/'
CATEGORY_SAVE_AS = 'categories/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'

FAVICON = "img/favicon.ico"

MATH_JAX = {
    "auto_insert": True,
    "process_summary": True,
    "align": "center",
    "tex": {
        "inlineMath": [["$", "$"], ['\\(','\\)']]
    },
    "process_summary": True,
    "equation_numbering": "AMS",
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('LinkedIn', 'https://www.linkedin.com/in/jsaundersee'),
#          ('GitHub', 'https://github.com/jay3ss'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/jsaundersee'),
          ('GitHub', 'https://github.com/jay3ss'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
