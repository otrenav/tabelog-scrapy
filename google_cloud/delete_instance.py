# -*- coding: utf-8 -*-

from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from oauth2client.client import ApplicationDefaultCredentialsError


def delete_instance(arguments):
    credentials = get_credentials()
    if credentials:
        print(50 * '-')
        print('DELETING GOOGLE CLOUD INSTANCE:')
        print('- Project:  {}'.format(arguments.project))
        print('- Zone:     {}'.format(arguments.zone))
        print('- Instance: {}'.format(arguments.instance))
        print(50 * '-')
        service = discovery.build(
            'compute',
            'v1',
            credentials=credentials
        )
        request = service.instances().delete(
            instance=arguments.instance,
            project=arguments.project,
            zone=arguments.zone
        )
        response = request.execute()
        pprint(response)


def get_credentials():
    try:
        credentials = GoogleCredentials.get_application_default()
    except ApplicationDefaultCredentialsError:
        credentials = None
    return(credentials)
