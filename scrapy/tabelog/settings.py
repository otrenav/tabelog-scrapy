# -*- coding: utf-8 -*-

BOT_NAME = 'tabelog'
USER_AGENT = 'ITAM'

DEPTH_LIMIT = 4
# LOG_LEVEL = 'INFO'
ROBOTSTXT_OBEY = True
AUTOTHROTTLE_DEBUG = False
AUTOTHROTTLE_ENABLED = True
SPIDER_MODULES = ['tabelog.spiders']
NEWSPIDER_MODULE = 'tabelog.spiders'
