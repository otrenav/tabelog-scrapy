# -*- coding: utf-8 -*-

import scrapy

from slugify import slugify
from bs4 import BeautifulSoup

from . import selectors


class RestaurantSpider(scrapy.Spider):

    name = "restaurants"
    allowed_domains = [ 'tabelog.com' ]
    start_urls = [ 'https://tabelog.com/en/' ]

    def parse(self, response):
        for prefecture_link in response.css(selectors.prefectures).extract():
            yield scrapy.Request(
                response.urljoin(prefecture_link + 'rstLst/'),
                callback=self._parse_prefecture_restaurants
            )

    def _parse_prefecture_restaurants(self, response):
        for restaurant_link in response.css(selectors.restaurants).extract():
            yield scrapy.Request(
                response.urljoin(restaurant_link),
                callback=self._parse_restaurant
            )

        next_page = response.css(selectors.next_page).extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(
                next_page,
                callback=self._parse_prefecture_restaurants
            )

    def _parse_restaurant(self, response):

        shop_headers = self._clean_headers(
            response.xpath(selectors.shop_headers).extract()
        )
        shop_data = self._clean_data(
            response.xpath(selectors.shop_data).extract()
        )
        self._assert_length(shop_headers, shop_data, "shop")

        seats_headers = self._clean_headers(
            response.xpath(selectors.seats_headers).extract()
        )
        seats_data = self._clean_data(
            response.xpath(selectors.seats_data).extract()
        )
        self._assert_length(seats_headers, seats_data, "seats")

        menu_headers = self._clean_headers(
            response.xpath(selectors.menu_headers).extract()
        )
        menu_data = self._clean_data(
            response.xpath(selectors.menu_data).extract()
        )
        self._assert_length(menu_headers, menu_data, "menu")

        features_headers = self._clean_headers(
            response.xpath(selectors.features_headers).extract()
        )
        features_data = self._clean_data(
            response.xpath(selectors.features_data).extract()
        )
        self._assert_length(features_headers, features_data, "features")

        restaurant_data =  {
            'top-name': response.xpath(selectors.top_name).extract_first(),
            'top-prefecture': response.xpath(selectors.top_prefecture).extract_first(),
            'top-category': response.xpath(selectors.top_category).extract_first(),
            'top-subcategory-one': response.xpath(selectors.top_subcategory_one).extract_first(),
            'top-subcategory-two': response.xpath(selectors.top_subcategory_two).extract_first(),
            'top-telephone': response.xpath(selectors.top_telephone).extract_first(),
            'top-nearest-station': response.xpath(selectors.top_nearest_station).extract_first(),
            'top-overall-score': response.xpath(selectors.top_overall_score).extract_first(),
            'top-night-score': response.xpath(selectors.top_night_score).extract_first(),
            'top-lunch-score': response.xpath(selectors.top_lunch_score).extract_first(),
            'top-budget-night': response.xpath(selectors.top_budget_night).extract_first(),
            'top-budget-lunch': response.xpath(selectors.top_budget_lunch).extract_first(),
            'top-comments': response.xpath(selectors.top_comments).extract_first(),
        }

        for idx, header in enumerate(shop_headers):
            restaurant_data["shop-" + header] = shop_data[idx]

        for idx, header in enumerate(seats_headers):
            restaurant_data["seats-" + header] = seats_data[idx]

        for idx, header in enumerate(menu_headers):
            restaurant_data["menu-" + header] = menu_data[idx]

        for idx, header in enumerate(features_headers):
            restaurant_data["features-" + header] = features_data[idx]

        restaurant_data['url'] = response.url

        yield restaurant_data

    def _clean_headers(self, headers_list):
        new_headers_list = []
        for header in headers_list:
            clean_header = slugify(header)
            if clean_header != "":
                new_headers_list.append(clean_header)
        return(new_headers_list)

    def _clean_data(self, data_list):
        new_data_list = []
        for data in data_list:
            dirty_data = BeautifulSoup(data)
            clean_data = " ".join(
                dirty_data.get_text()
                .replace("\n", " ")
                .replace("\r", " ")
                .strip()
                .split()
            )
            new_data_list.append(clean_data)
        return(new_data_list)

    def _assert_length(self, headers, data, section):
        if len(headers) != len(data):
            print('!' * 60)
            print('!' * 60)
            print(headers)
            print(data)
            print('!' * 60)
            print('!' * 60)
            raise ValueError(
                "Headers and data for " +
                "{0} have different lengths ({1} vs {2})".format(
                    section, len(headers), len(data)
                )
            )
