#!/usr/bin/env python3

import boto3

AWS_REGION = "us-east-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
VOLUME_ID = 'vol-04fcb3a77c970e425'

snapshot = EC2_RESOURCE.create_snapshot(
    VolumeId=VOLUME_ID,
    TagSpecifications=[
        {
            'ResourceType': 'snapshot',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'hands-on-cloud-ebs-snapshot'
                },
            ]
        },
    ]
)

print(f'Snapshot {snapshot.id} created for volume {VOLUME_ID}')
