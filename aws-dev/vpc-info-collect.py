import boto3

ec2 = boto3.client('ec2')

vpc_info = ec2.describe_vpcs(
    VpcIds=[
        'vpc-699ca80c'
    ],
)

print(vpc_info)