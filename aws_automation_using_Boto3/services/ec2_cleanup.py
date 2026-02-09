import boto3
import logging

ec2 = boto3.client("ec2", region_name="ap-south-1")

# Find all the EC2 instances which are in stopped state
def list_stopped_ec2():
    response = ec2.describe_instances(
        Filters=[
            {"Name": "instance-state-name", "Values": ["stopped"]}
        ]
    )

    stopped_instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            logging.info(f"Instance ID: {instance['InstanceId']}")
            logging.info(f"State: {instance['State']['Name']}")
            logging.info(f"Instance Type: {instance['InstanceType']}")
            logging.info("-" * 30)

            stopped_instances.append(
                f"{instance['InstanceId']} | {instance['InstanceType']} | {instance['State']['Name']}"
            )

    return stopped_instances
