import boto
import boto.s3.connection
import os

access_key = os.environ['ACCESS_KEY']
secret_key = os.environ['SECRET_KEY']
s3_host = os.environ['https://s3.eu-west-1.amazonaws.com']

conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = s3_host,
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

for bucket in conn.get_all_buckets():
        print("{name}\t{created}".format(
                name = bucket.name,
                created = bucket.creation_date,
        ))