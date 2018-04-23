# -*- coding: utf-8 -*-

BUCKET = 'tabelog-scraping-results'

OPTIONS = ['project=', 'instance=', 'zone=', 'prefecture=']

TOGETHER = ['--project', '--instance', '--zone']

USAGE = """
Usage:

$ python main.py --project=<google_cloud_project>
                 --zone=<google_cloud_zone>
                 --instance=<google_cloud_instance>
                 --prefecture=<prefecture>
"""
