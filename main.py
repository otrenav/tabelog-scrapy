# -*- coding: utf-8 -*-

import os
import sys
import getopt

from helpers import constants
from helpers.arguments import Arguments
from google_cloud.cloud_storage import store_results
from google_cloud.delete_instance import delete_instance


class Main(object):

    def __init__(self, argv):
        self.arguments = self._get_arguments(argv)

    def execute(self):
        self._crawl_restaurants()
        if self._in_google_cloud():
            self._store_results()
            self._delete_instance()
        self._finished_message()

    def _crawl_restaurants(self):
        os.chdir(self.arguments.scrapy_directory)
        os.system(self._scrapy_command())

    def _in_google_cloud(self):
        return self.arguments.project is not None

    def _store_results(self):
        store_results(self.arguments)

    def _delete_instance(self):
        delete_instance(self.arguments)

    def _scrapy_command(self):
        if self.arguments.prefectures and not self.arguments.category_groups:
            return('{} -a prefectures={}'.format(
                self.arguments.scrapy_command,
                self.arguments.prefecture
            ))
        elif not self.arguments.prefectures and self.arguments.category_groups:
            return('{} -a category_groups={}'.format(
                self.arguments.scrapy_command,
                self.arguments.category_groups
            ))
        elif self.arguments.prefectures and self.arguments.category_groups:
            return('{} -a prefectures={} -a category_groups={}'.format(
                self.arguments.scrapy_command,
                self.arguments.prefectures,
                self.arguments.category_groups
            ))
        return(self.arguments.scrapy_command)

    def _get_arguments(self, argv):
        try:
            args, _ = getopt.getopt(argv, '', constants.OPTIONS)
        except getopt.GetoptError:
            print(constants.USAGE)
            sys.exit('Error: could not parse arguments\n')
        return(Arguments(args))

    def _finished_message(self):
        print(50 * '-')
        print('FINISHED')
        print(50 * '-')


if __name__ == '__main__':
    Main(sys.argv[1:]).execute()
