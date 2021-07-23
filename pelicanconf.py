#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import datetime
AUTHOR = 'CamilaEBF'
SITENAME = 'CamilaEBF'
SITEURL = 'http://localhost:8080'

PATH = 'content'

TIMEZONE = 'America/Buenos_Aires'

DEFAULT_LANG = 'es'
DATE_FORMATS = {
    "es": "%d-%m-%Y",
}

USE_FOLDER_AS_CATEGORY = False
COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 7

# Theme Settings
SITELOGO = "/images/title.png"
FAVICON = "/images/favicon.png"
THEME = "themes/Flex"
PYGMENTS_STYLE = "default"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Main Menu
MAIN_MENU = True
MENUITEMS = (("Archives", "/archives"), ("Categories", "/categories"), ("Tags", "/tags"),)

# Blogroll
LINKS = (("Project", "https://github.com/CamilaEBF/camilaebf.github.io"),)

# Social widget
SOCIAL = (
    ("linkedin", "https://www.linkedin.com/in/camilablancfick/"),
    ("github", "https://github.com/CamilaEBF")
)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True