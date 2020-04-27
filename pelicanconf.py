#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = "/home/estuardolh/pelican-themes/taman/"

AUTHOR = u'Estuardo López'
SITENAME = u'Estuardo info'
SITEURL = ''
DESCRIPTION = u'Estuardo López'
PATH = 'content'

TIMEZONE = 'America/Guatemala'

DEFAULT_LANG = u'en'
#A programming lover.
# Feed generation is usually not desired when developing
BIO = u'<h3>ESTUARDO LÓPEZ</h3><p>Engineering student and programming lover.</p>'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('', ''),)
SECTIONS = (('🏡','https://estuardo.info')
  ,('Resume', '/resume.pdf')
  , ('Repos', 'https://github.com/estuardolh')
  , ('Bio', '/bio'),)
# Social widget
SOCIAL = ((),)

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
