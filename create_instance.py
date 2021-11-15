# import boto3 package
import boto3

# Let's use Amazon EC2
AWS_REGION = 'us-east-1'
EC2_CLIENT = boto3.client('ec2', region_name=AWS_REGION)
SNAPSHOT_ID = 'snap-0ab85991b914b6357'

# create a AMI from snapshot
ami = EC2_CLIENT.register_image(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'Ebs': {
                'DeleteOnTermination': True,
                'SnapshotId': SNAPSHOT_ID,
                'VolumeSize': 20,
                'VolumeType': 'gp2'
            }
        },
    ],
    Description='hands-on-cloud-ebs-boto3-ami-from-snapshot',
    Name='hands-on-cloud-ebs-boto3-ami-from-snapshot',
    RootDeviceName='/dev/xvda',
    VirtualizationType='hvm'
)

# print the resource ID of created EBS volume
print(ami)
