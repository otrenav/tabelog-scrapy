# -*- coding: utf-8 -*-

from google.auth.exceptions import DefaultCredentialsError
from google.cloud import storage

from helpers.constants import BUCKET


def store_results(arguments):
    client = get_client()
    if client:
        print(50 * '-')
        print('SAVING RESULTS TO GOOGLE CLOUD STORAGE')
        print('- Bucket: {}'.format(BUCKET))
        print('- File:   {}'.format(arguments.file))
        print(50 * '-')
        if not client.lookup_bucket(BUCKET):
            client.create_bucket(BUCKET)
        bucket = client.get_bucket(BUCKET)
        blob = bucket.blob(arguments.file)
        blob.upload_from_filename(arguments.file)


def get_client():
    try:
        client = storage.Client()
    except DefaultCredentialsError:
        client = None
    return(client)
