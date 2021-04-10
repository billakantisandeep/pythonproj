import boto3
ec2 = boto3.resource(ec2)

#Create VPC
vpc = ec2.create_vpc(CidrBlock='172.16.0.0/16')

