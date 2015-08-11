#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Beatson Group'
SITENAME = u'Beatson Microbial Genomics Lab'
SITEURL = ''

TIMEZONE = 'Australia/Brisbane'

DEFAULT_LANG = u'en'

STATIC_PATHS = ['images', 'downloads' , 'schedule']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Code on GitHub', 'https://github.com/organizations/BeatsonLab-MicrobialGenomics'),
        ('SCMB@UQ', 'http://staff.scmb.uq.edu.au/staff/scott-beatson'),
        ('BRIG', 'http://sourceforge.net/projects/brig/'),
        ('EasyFig', 'http://easyfig.sourceforge.net'),
        ('SeqFindR', 'http://github.com/mscook/SeqFindR'),)

# Social widget
SOCIAL = ''

DEFAULT_PAGINATION = 5

CWD = os.getcwd()
THEME = os.path.join(CWD, "themes/pelican-bootstrap3")
FAVICON = 'images/favicon.png'
SITESUBTITLE = 'Microbial Genomics Laboratory'
CUSTOM_LICENSE=' 2013-2015 Beatson Microbial Genomics Laboratory '


#Tweak visually
DISPLAY_CATEGORIES_ON_MENU = False
#About.rst  Data.rst  People  People.rst  Projects.rst  Publications.rst  Software.rst
MENUITEMS = [('About','http://beatsonlab.com'),
             ('Blog', 'http://beatsonlab.com/archives'),
             ('Data','http://beatsonlab.com/pages/data.html'),
             ('People','http://beatsonlab.com/pages/people.html'),
             ('Projects', 'http://beatsonlab.com/pages/projects.html'),
             ('Publications','http://beatsonlab.com/pages/publications.html'),
             ('Software','http://beatsonlab.com/pages/software.html')]
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = False
#MENUITEMS = 'Publications'

# Theme specific options for GitHub
GITHUB_USER = 'BeatsonLab-MicrobialGenomics'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True

#Theme specific - Use bootswatch themes
BOOTSTRAP_THEME='yeti'

GOOGLE_ANALYTICS='UA-49094461-1'

#PLUGIN_PATH = 'pelican-plugins/'
#PLUGINS = ['better_figures_and_images']
#RESPONSIVE_IMAGES = True

#New 11/08/2015
BOOTSTRAP_FLUID = True
