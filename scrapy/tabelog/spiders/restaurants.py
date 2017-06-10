# -*- coding: utf-8 -*-

import scrapy

from slugify import slugify
from bs4 import BeautifulSoup

import selectors
import constants


class RestaurantSpider(scrapy.Spider):

    name = 'restaurants'
    base_url = 'https://tabelog.com/en/'
    allowed_domains = ['tabelog.com']

    def __init__(self, prefecture=None, *args, **kwargs):
        prefectures = self._get_prefectures(prefecture)
        self.start_urls = [
            '{}{}/rstLst/{}/?SrtT=rt&Srt=D'.format(self.base_url, p, c)
            for p in prefectures
            for c in constants.categories
        ]

        print(50 * "*")
        print(len(self.start_urls))
        print(self.start_urls)
        self.all_urls = []
        self.n_length_errors = 0
        print(50 * "*")

        super(RestaurantSpider, self).__init__(*args, **kwargs)

    def _get_prefectures(self, prefecture):
        if prefecture:
            return([prefecture])
        return(constants.prefectures)

    def parse(self, response):
        restaurants = response.css(selectors.restaurants).extract()

        self.all_urls += restaurants
        with open('all_urls.txt', 'w') as thefile:
            for url in self.all_urls:
                thefile.write("{}\n".format(url))

        for restaurant in restaurants:
            yield scrapy.Request(
                response.urljoin(restaurant),
                callback=self._parse_restaurant
            )

        next_page = response.css(selectors.next_page).extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(
                next_page,
                callback=self.parse
            )

    def _parse_restaurant(self, response):

        shop_headers = self._clean_headers(
            response.xpath(selectors.shop_headers).extract()
        )
        shop_data = self._clean_data(
            response.xpath(selectors.shop_data).extract()
        )
        self._assert_length(shop_headers, shop_data, 'shop')

        seats_headers = self._clean_headers(
            response.xpath(selectors.seats_headers).extract()
        )
        seats_data = self._clean_data(
            response.xpath(selectors.seats_data).extract()
        )
        self._assert_length(seats_headers, seats_data, 'seats')

        menu_headers = self._clean_headers(
            response.xpath(selectors.menu_headers).extract()
        )
        menu_data = self._clean_data(
            response.xpath(selectors.menu_data).extract()
        )
        self._assert_length(menu_headers, menu_data, 'menu')

        features_headers = self._clean_headers(
            response.xpath(selectors.features_headers).extract()
        )
        features_data = self._clean_data(
            response.xpath(selectors.features_data).extract()
        )
        self._assert_length(features_headers, features_data, 'features')

        print('*' * 50)
        print("n_length_errors: {}".format(self.n_length_errors))
        print('*' * 50)

        restaurant_data = {
            'top-name': self._first(
                response,
                'top_name'
            ),
            'top-prefecture': self._first(
                response,
                'top_prefecture'
            ),
            'top-category': self._first(
                response,
                'top_category'
            ),
            'top-subcategory-one': self._first(
                response,
                'top_subcategory_one'
            ),
            'top-subcategory-two': self._first(
                response,
                'top_subcategory_two'
            ),
            'top-telephone': self._first(
                response,
                'top_telephone'
            ),
            'top-nearest-station': self._first(
                response,
                'top_nearest_station'
            ),
            'top-overall-score': self._first(
                response,
                'top_overall_score'
            ),
            'top-night-score': self._first(
                response,
                'top_night_score'
            ),
            'top-lunch-score': self._first(
                response,
                'top_lunch_score'
            ),
            'top-budget-night': self._first(
                response,
                'top_budget_night'
            ),
            'top-budget-lunch': self._first(
                response,
                'top_budget_lunch'
            ),
            'top-comments': self._first(
                response,
                'top_comments'
            )
        }

        for idx, header in enumerate(shop_headers):
            restaurant_data['shop-' + header] = shop_data[idx]

        for idx, header in enumerate(seats_headers):
            restaurant_data['seats-' + header] = seats_data[idx]

        for idx, header in enumerate(menu_headers):
            restaurant_data['menu-' + header] = menu_data[idx]

        for idx, header in enumerate(features_headers):
            restaurant_data['features-' + header] = features_data[idx]

        restaurant_data['url'] = response.url

        yield restaurant_data

    def _clean_headers(self, headers_list):
        new_headers_list = []
        for header in headers_list:
            clean_header = slugify(header)
            if clean_header != '':
                new_headers_list.append(clean_header)
        return(new_headers_list)

    def _clean_data(self, data_list):
        new_data_list = []
        for data in data_list:
            dirty_data = BeautifulSoup(data)
            clean_data = ' '.join(
                dirty_data.get_text()
                .replace('\n', ' ')
                .replace('\r', ' ')
                .strip()
                .split()
            )
            new_data_list.append(clean_data)
        return(new_data_list)

    def _assert_length(self, headers, data, section):
        self.n_length_errors += 1

        print("-" * 50)
        print("Section")
        print(section)
        print("Headers")
        print(headers)
        print("Data")
        print(data)
        print("-" * 50)

        if len(headers) != len(data):
            print('!' * 60)
            print(headers)
            print(data)
            print('!' * 60)
            raise ValueError(
                'Headers and data for ' +
                '{0} have different lengths ({1} vs {2})'.format(
                    section, len(headers), len(data)
                )
            )

    def _first(self, response, selector):
        selector = getattr(selectors, selector)
        return(response.xpath(selector).extract_first())
