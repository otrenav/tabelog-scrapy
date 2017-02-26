# -*- coding: utf-8 -*-

BOT_NAME = 'tabelog'

SPIDER_MODULES = ['tabelog.spiders']
NEWSPIDER_MODULE = 'tabelog.spiders'
USER_AGENT = 'ITAM'

ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS = 32

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = False

# DOWNLOAD_DELAY = 3
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16
# COOKIES_ENABLED = False
# TELNETCONSOLE_ENABLED = False

# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# SPIDER_MIDDLEWARES = {
#    'tabelog.middlewares.TabelogSpiderMiddleware': 543,
# }

# DOWNLOADER_MIDDLEWARES = {
#    'tabelog.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# ITEM_PIPELINES = {
#    'tabelog.pipelines.TabelogPipeline': 300,
# }

# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
