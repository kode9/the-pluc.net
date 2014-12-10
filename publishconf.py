#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Publication pelican configuration file

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

AUTHOR        = 'Pierre-Luc Perrier'
SITENAME      = 'Pluc'
SITEURL       = 'https://the-pluc.net'
RELATIVE_URLS = False
DEFAULT_LANG  = 'fr'
TIMEZONE      = 'Europe/Paris'

FEED_ALL_ATOM      = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION        = ('.git')

# Disable feed generation
FEED_ALL_ATOM         = None
CATEGORY_FEED_ATOM    = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM      = None
AUTHOR_FEED_RSS       = None

# Disable tag generation
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
