import os
import sys 
#sys.path.append('..')
#from AWSS3.aws_bucket_client import bucket_client
#from config import Config
import boto3


def main():
    print(len(sys.argv))
    if (len(sys.argv)!=6):
        print('Error: Required 5 arguments.')
        sys.exit(1)
    
    folder = sys.argv[1]
    s3_bucket = sys.argv[2]
    s3_secret_access_key = sys.argv[3]
    s3_access_key = sys.argv[4]
    s3_region = sys.argv[5]

    s3_client = boto3.client(service_name = "s3",
        region_name = s3_region,
        aws_access_key_id = s3_access_key,
        aws_secret_access_key = s3_secret_access_key,
    )

    # s3_client = session.client()

    root = "scripts/" + folder
    print('here')
    print(os.listdir())
    for path, subdirs, files in os.walk(root):
        print('here1')
        if 'pycache' in path.split('\\')[-1]:
            continue
        print('here2')
        for file in files:
            full_path = os.path.join(path, file)
            dest_path = full_path.split('..\\')[-1].replace('\\', '/')
            try:
                print('Uploading file: ' + dest_path)
                s3_client.upload_file(full_path,
                                    s3_bucket,
                                    dest_path,
                                    )
                print('Upload succesfull!')

            except Exception as e:
                # This is a catch all exception
                print("Error happened when uploading the file: ", e)
                return e

main()