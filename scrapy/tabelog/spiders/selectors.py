# -*- coding: utf-8 -*-

#
# Crawling selectors
#
prefectures = '.index-area__list-items li a::attr(href)'
restaurants = '.list-rst__name a::attr(href)'
next_page   = '.c-pagination__target--next::attr(href)'

#
# Scraping selectors
#

# Headers
shop_headers     = "//*[@id='anchor-rd-detail']/section[1]/table/tbody/tr/th/text()"
seats_headers    = "//*[@id='anchor-rd-detail']/section[2]/table/tbody/tr/th/text()"
menu_headers     = "//*[@id='anchor-rd-detail']/section[3]/table/tbody/tr/th/text()"
features_headers = "//*[@id='anchor-rd-detail']/section[4]/table/tbody/tr/th/text()"

# Data
shop_data     = "//*[@id='anchor-rd-detail']/section[1]/table/tbody/tr/td[descendant-or-self::text()]"
seats_data    = "//*[@id='anchor-rd-detail']/section[2]/table/tbody/tr/td[descendant-or-self::text()]"
menu_data     = "//*[@id='anchor-rd-detail']/section[3]/table/tbody/tr/td[descendant-or-self::text()]"
features_data = "//*[@id='anchor-rd-detail']/section[4]/table/tbody/tr/td[descendant-or-self::text()]"

# Top
top_variables = {
    'top-name'            : '/html/body/article/header/div[1]/div/div[1]/h2/a/text()',
    'top-prefecture'      : '/html/body/article/header/div[1]/div/div[2]/div/div/dl[1]/dd/div/p/a/span/text()',
    'top-category'        : '/html/body/article/header/div[1]/div/div[2]/div/div/dl[2]/dd/div[1]/p/a/span/text()',
    'top-subcategory_one' : '/html/body/article/header/div[1]/div/div[2]/div/div/dl[2]/dd/div[2]/p/a/span/text()',
    'top-subcategory_two' : '/html/body/article/header/div[1]/div/div[2]/div/div/dl[2]/dd/div[3]/p/a/span/text()',
    'top-telephone'       : '/html/body/article/header/div[1]/div/div[2]/div/div/dl[3]/dd/text()',
    'top-nearest_station' : '/html/body/article/header/div[1]/div/div[2]/div/div/dl[1]/dd/text()',
    'top-overall_score'   : '/html/body/article/header/div[1]/div/div[2]/div/ul/li[1]/b/text()',
    'top-night_score'     : '/html/body/article/header/div[1]/div/div[2]/div/ul/li[3]/b/text()',
    'top-lunch_score'     : '/html/body/article/header/div[1]/div/div[2]/div/ul/li[4]/b/text()',
    'top-budget_night'    : '/html/body/article/header/div[1]/div/div[2]/div/div/dl[4]/dd/p[1]/b/text()',
    'top-budget_lunch'    : '/html/body/article/header/div[1]/div/div[2]/div/div/dl[4]/dd/p[2]/b/text()',
    'top-comments'        : '/html/body/article/header/div[1]/div/div[2]/div/ul/li[5]/a/b/text()'
}
