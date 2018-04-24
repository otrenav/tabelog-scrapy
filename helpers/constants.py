# -*- coding: utf-8 -*-

BUCKET = 'tabelog-scraping-results'

OPTIONS = [
    'project=',
    'instance=',
    'zone=',
    'prefectures=',
    'category_groups='
]

TOGETHER = [
    '--project',
    '--instance',
    '--zone'
]

USAGE = """
Usage:

$ python main.py --project=<google_cloud_project>
                 --zone=<google_cloud_zone>
                 --instance=<google_cloud_instance>
                 --prefectures=<prefecture>,<prefecture>,...
                 --category_groups=<group_number>,<group_number>,...
"""
