# create ec2 instance
import boto3

def create_ec2_instance():
    try:
      print("create ec2 instance")
      resource_ec2 = boto3.client("ec2")
      resource_ec2.run_instances(
        ImageId ="ami-08df646e18b182346",
        MinCount =1,
        MaxCount =1,
        InstanceType ="t2.micro",
        KeyName ="cloud"
      )
    except Exception as e:
      print(e)

create_ec2_instance()
