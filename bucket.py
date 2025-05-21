import boto3 
s3 = boto3.resource("s3")
def show_bucket(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)
def create_bucket(s3,bucket_name,region):
    s3.create_bucket(Bucket = "buck-buvket-for-red",
        CreateBuckerConfiguration= {
            'locationConstraint': 'eu-north-1'
    })

def upload_backup(s3,file_name,bucket_name,key_name):
    data= open(file_name,"rb")
    s3.Bucket(bucket_name).put_object(key=key_name,body=data)

bucket_name = "buck-buvket-for-red"
region = 'eu-north-1'
file_name = ' '
upload_backup(s3,filebucket_name,bucket_name,my_backupkey)