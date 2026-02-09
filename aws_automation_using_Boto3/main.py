import boto3
import logging
import os
import smtplib
from email.mime.text import MIMEText


# Step 0: Make sure Logs folder exists
if not os.path.exists("Logs"):
    os.makedirs("Logs")


# Step 1: Setup logging
logging.basicConfig(
    filename="Logs/aws_cleanup.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("AWS Cost Optimization Script Started")


ec2 = boto3.client("ec2", region_name="ap-south-1")


# Step 3: Get list of all EC2 instances
response = ec2.describe_instances()

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        logging.info(f"Instance_Id: {instance['InstanceId']}")
        logging.info(f"State: {instance['State']['Name']}")
        logging.info(f"InstanceType: {instance['InstanceType']}")
        logging.info("-" * 40)


# Step 4: Import service functions
from services.ec2_cleanup import list_stopped_ec2
from services.ebs_cleanup import list_unattached_ebs
from services.eip_cleanup import list_unused_elastic_ips
from services.snapshot_cleanup import list_old_snapshots

logging.info("Checking stopped EC2 instances...")
stopped_ec2 = list_stopped_ec2()

logging.info("Checking unused EBS volumes...")
unused_ebs = list_unattached_ebs()

logging.info("Checking unused Elastic IPs...")
unused_eip = list_unused_elastic_ips()

logging.info("Checking old EBS snapshots...")
old_snapshots = list_old_snapshots()

logging.info("Scan completed. No resources were deleted.")
logging.info("-" * 40)


# Step 5: Prepare email content
email_body = "AWS Cost Optimization Report\n\n"

email_body += "Stopped EC2 instances:\n"
email_body += "\n".join(stopped_ec2) if stopped_ec2 else "None"
email_body += "\n\n"

email_body += "Unused EBS volumes:\n"
email_body += "\n".join(unused_ebs) if unused_ebs else "None"
email_body += "\n\n"

email_body += "Unused Elastic IPs:\n"
email_body += "\n".join(unused_eip) if unused_eip else "None"
email_body += "\n\n"

email_body += "Old Snapshots:\n"
email_body += "\n".join(old_snapshots) if old_snapshots else "None"


# Step 6: Send email
def send_email(subject, body, to_email):
    from_email = "rpsingh98188@gmail.com"
    from_password = "ivur ltsx yksu ajpk"   # App Password

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_email, from_password)
        server.send_message(msg)

send_email("AWS Cloud Report", email_body, "chauhantaruna591@gmail.com")

logging.info("Email sent successfully")
