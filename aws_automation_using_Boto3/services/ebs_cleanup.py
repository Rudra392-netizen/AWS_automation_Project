import boto3
import logging

ec2 = boto3.client("ec2")

# Find all the EBS volumes which are not attached to any EC2 instance
def list_unattached_ebs():
    response = ec2.describe_volumes(
        Filters=[
            {"Name": "status", "Values": ["available"]}
        ]
    )

    unused_volumes = []

    for volume in response["Volumes"]:
        logging.info(f"Volume ID: {volume['VolumeId']}")
        logging.info(f"Size (GB): {volume['Size']}")
        logging.info(f"AZ: {volume['AvailabilityZone']}")
        logging.info("-" * 30)

        unused_volumes.append(
            f"{volume['VolumeId']} | {volume['Size']}GB | {volume['AvailabilityZone']}"
        )

    return unused_volumes
