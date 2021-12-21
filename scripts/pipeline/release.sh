#!/bin/bash

folder=$1
s3_bucket=$2
s3_secret_access_key=$3
s3_access_key=$4
s3_region=$5

# Install required dependencies for Python script
pip3 install boto3

# Run upload script

python3 scripts/pipeline/upload_model_folder_to_s3.py $folder $s3_bucket $s3_secret_access_key $s3_access_key $s3_region
