import boto3
import logging

# Here I will list all the Elastic IPs that are not attached to any EC2 instance
ec2 = boto3.client("ec2")

def list_unused_elastic_ips():
    response = ec2.describe_addresses()

    unused_eips = []

    if not response["Addresses"]:
        logging.info("No Elastic IP found")
        return unused_eips

    for ip in response["Addresses"]:
        if "InstanceId" not in ip:
            logging.info(f"Unused Elastic IP: {ip['PublicIp']}")
            unused_eips.append(ip["PublicIp"])

    return unused_eips
