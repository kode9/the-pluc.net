#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Development pelican configuration file

AUTHOR        = 'Pierre-Luc Perrier'
SITENAME      = 'Pluc'
SITEURL       = ''
RELATIVE_URLS = True
DEFAULT_LANG  = 'fr'
TIMEZONE      = 'Europe/Paris'
THEME         = 'abzhack'

PATH          = 'content'
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False

SUMMARY_MAX_LENGTH = 20

# Pagination
## The minimum number of articles allowed on the last page
DEFAULT_ORPHANS = 1
## The maximum number of articles to include on a page, not including
## orphans. False to disable pagination.
DEFAULT_PAGINATION = False
# A set of patterns that are used to determine advanced pagination output.
# PAGINATION_PATTERNS = (
#     (1, '{base_name}/', '{base_name}/index.html'),
#     (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
# )

# Feed generation is usually not desired when developing
FEED_ALL_ATOM         = None
CATEGORY_FEED_ATOM    = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM      = None
AUTHOR_FEED_RSS       = None

# Disable tag generation
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('github', 'https://github.com/kode9'),
)
