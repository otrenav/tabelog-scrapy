# -*- coding: utf-8 -*-

import sys
import datetime
import constants


class Arguments(object):

    SCRAPY_DIRECTORY = './scrapy/'
    SCRAPY_COMMAND = 'scrapy crawl restaurants -o '
    DATE = datetime.datetime.now().strftime('%Y-%m-%d')

    def __init__(self, args):
        self.arguments = dict(args)
        self._check_google_cloud_arguments()

    @property
    def project(self):
        return(self.arguments['--project'])

    @property
    def zone(self):
        return(self.arguments['--zone'])

    @property
    def instance(self):
        return(self.arguments['--instance'])

    @property
    def prefecture(self):
        return(self.arguments.get('--prefecture', None))

    @property
    def file(self):
        if self.prefecture:
            return('{}-{}.csv'.format(self.prefecture, self.DATE))
        return('all-prefectures-{}.csv'.format(self.DATE))

    @property
    def scrapy_directory(self):
        return(self.SCRAPY_DIRECTORY)

    @property
    def scrapy_command(self):
        return(self.SCRAPY_COMMAND + self.file)

    def _check_google_cloud_arguments(self):
        google_cloud_arguments = [
            a in self.arguments.keys()
            for a in constants.TOGETHER
        ]
        if any(google_cloud_arguments):
            if not all(google_cloud_arguments):
                print(constants.USAGE)
                sys.exit(
                    'Error: if any Google Cloud parameter ' +
                    'is sent, all must be sent.\n'
                )
