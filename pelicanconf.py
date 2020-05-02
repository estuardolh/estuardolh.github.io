#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = "/home/estuardolh/pelican-themes/tam/"

AUTHOR = u'Estuardo López'
SITENAME = u'Estuardo info'
SITEURL = 'estuardo.info'
DESCRIPTION = u'Estuardo López'
PATH = 'content'
#DATE_FORMATS = {
#    'en': '%a, %d %b %Y',
#}
#LOCALE = ('en_US.UTF-8'
#    )


TIMEZONE = 'America/Guatemala'

DEFAULT_LANG = u'en'
BIO = u'<h3>ESTUARDO LÓPEZ</h3><p>Engineering student and programming lover.</p>'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('', ''),)
SECTIONS = (('Home','https://estuardo.info')
  , ('Repos', 'https://github.com/estuardolh')
  , ('Resume', '/resume.pdf')
  ,)
# Social widget
SOCIAL = ((),)

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
