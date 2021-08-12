from boto3.session import Session
from botocore.client import Config
from botocore.handlers import set_list_objects_encoding_type_url

import boto3
import os

s3_access_key = os.environ['S3_ACCESS_KEY']
s3_secret_key = os.environ['S3_SECRET_KEY']
s3_host = os.environ['S3_HOST']
s3_region = os.environ['S3_REGION']

#boto3.set_stream_logger('')

session = Session(aws_access_key_id=s3_access_key, aws_secret_access_key=s3_secret_key, region_name=s3_region)

session.events.unregister('before-parameter-build.s3.ListObjects', set_list_objects_encoding_type_url)

s3 = session.resource('s3', endpoint_url=s3_host, config=Config(signature_version='s3v4'))

buckets = s3.buckets.all()
for bucket in buckets:
    print("############### BUCKET ###############")
    print(bucket)
    print("+++++++++++++++ OBJECTS ++++++++++++++")
    for f in bucket.objects.all():
        print(f.key)
    print("######################################")