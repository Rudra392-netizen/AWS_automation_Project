import boto3
import datetime
import logging

ec2 = boto3.client("ec2")

# Find all the old EBS snapshots
def list_old_snapshots():
    response = ec2.describe_snapshots(OwnerIds=["self"])

    old_snapshots = []

    for snapshot in response["Snapshots"]:
        snapshot_date = snapshot["StartTime"].date()
        today = datetime.date.today()

        age = (today - snapshot_date).days

        if age == 0:
            logging.info(f"Old Snapshot ID: {snapshot['SnapshotId']}")
            logging.info(f"Age: {age}")
            logging.info("-" * 40)

            old_snapshots.append(
                f"{snapshot['SnapshotId']} | Age: {age} days"
            )

    return old_snapshots
