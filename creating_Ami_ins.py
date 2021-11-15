#!/usr/bin/env python3

import boto3

AWS_REGION = "us-east-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
EC2_INSTANCE_ID = 'i-0561cc6f9dd97f880'

instance = EC2_RESOURCE.Instance(EC2_INSTANCE_ID)

image = instance.create_image(
    Name='hands-on-cloud-demo-ami',
    Description='This is demo AMI',
    NoReboot=True
)

print(f'AMI creation started: {image.id}')

image.wait_until_exists(
    Filters=[
        {
            'Name': 'state',
            'Values': ['available']
        }
    ]
)

print(f'AMI {image.id} successfully created')
