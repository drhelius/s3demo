from boto3.session import Session
from botocore.client import Config

import os
import time
import boto3
import uuid

#############
def list_buckets_and_objects():
    buckets = s3.list_buckets()

    print("> Listing Buckets:")

    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print("   " + bucket['Name'])

        objects = s3.list_objects(Bucket=bucket['Name'])

        if "Contents" in objects:
            print("    Listing objects in bucket:")
            for obj in objects['Contents']:
                print("     Key: " + obj['Key'] + ". Size: "+ str(obj['Size']))
            print("    End of bucket")
        else:
            print("    This bucket is empty")
#############
def create_demo_bucket():
    print("> Creating new bucket '" + bucket_name + "'")
    bucket = s3.create_bucket(Bucket=bucket_name,
                             CreateBucketConfiguration={'LocationConstraint': s3_region})

    print("> Creating new object 'demo'")
    s3.put_object(Body=b'This is a test of S3', Bucket=bucket_name, Key='demo')
#############
def delete_demo_bucket():
    print("> Deleting object 'demo' in bucket '" + bucket_name + "'")
    s3.delete_object(Bucket=bucket_name, Key='demo')

    print("> Deleting bucket '" + bucket_name + "'")
    s3.delete_bucket(Bucket=bucket_name)
#############

s3_access_key = os.environ['S3_ACCESS_KEY']
s3_secret_key = os.environ['S3_SECRET_KEY']
s3_host = os.environ['S3_HOST']

if "S3_REGION" in os.environ:
    s3_region = os.environ['S3_REGION']
else:
    s3_region = ""

bucket_name = uuid.uuid4().hex

#boto3.set_stream_logger('')

session = boto3.session.Session()

s3 = session.client(
    service_name='s3',
    aws_access_key_id=s3_access_key,
    aws_secret_access_key=s3_secret_key,
    endpoint_url=s3_host,
)

while True:
    print("> BEGIN")

    list_buckets_and_objects()
    create_demo_bucket()
    list_buckets_and_objects()
    delete_demo_bucket()
    list_buckets_and_objects()

    print("> END")

    time.sleep(60)