import boto3

ec2 = boto3.client('ec2')
vpc_id = 'vpc_id'

vpc_info = ec2.describe_vpcs(
    VpcIds=[
        vpc_id
    ],
)

print(vpc_info)