AWS Cost Optimization & Monitoring Automation (Python + Boto3)
📌 Why I Built This Project

In real companies, AWS bills increase silently because unused resources keep running in the background.
Many beginners only create EC2, EBS, snapshots etc., but real DevOps work is about monitoring and optimization.

I built this project to:

Understand how unused AWS resources increase cost

Learn real-world AWS automation using Python (boto3)

Practice logging, modular code structure, and email alerts

Build a production-style DevOps project, not just a script

Show interviewers that I can think like a DevOps engineer

This project does NOT delete anything.
It only scans, reports, logs, and sends email alerts — which is safer and more realistic for production.

🧠 What Problem This Project Solves

In AWS accounts, these resources often remain unused:

❌ Stopped EC2 instances

❌ Unattached EBS volumes

❌ Unused Elastic IPs

❌ Old EBS snapshots

Even if they are unused, AWS still charges money.

This project automatically:

Scans AWS account

Finds unused resources

Logs all details

Sends a detailed email report

Helps teams take action manually

🧱 Project Structure
aws-cost-optimization/
│
├── main.py
├── services/
│   ├── ec2_cleanup.py
│   ├── ebs_cleanup.py
│   ├── eip_cleanup.py
│   ├── snapshot_cleanup.py
│
├── Logs/
│   └── aws_cleanup.log
│
├── README.md

🛠️ Technologies Used

Python

AWS SDK (boto3)

SMTP (Email automation)

Logging module

AWS Services

EC2

EBS

Elastic IP

Snapshots

🔍 What Each File Does
main.py

This is the controller file.

It does:

Logging setup

Calls AWS service scripts

Collects results

Prepares email report

Sends email notification

services/ec2_cleanup.py

Finds stopped EC2 instances

Stores instance IDs in a list using .append()

Returns the list to main.py

services/ebs_cleanup.py

Finds unattached EBS volumes

Appends volume IDs to a list

Returns data for email + logging

services/eip_cleanup.py

Finds unused Elastic IPs

Collects public IP details

Returns list

services/snapshot_cleanup.py

Finds old EBS snapshots

Helps identify storage wastage

🧾 Why We Used .append() in Services Files

This is very important (interview question 🔥).

Earlier, scripts only printed data.
But printing is useless for automation.

We used .append() because:

We need to store results

We need to reuse data

We need to send dynamic email reports

Example:

stopped_instances.append(instance_id)


This allows:

Returning data to main.py

Joining results into email body

Writing reusable code

👉 Without .append(), email automation is impossible

📂 Logging Explanation

We created a Logs/ folder and log file.

Why logging?

Production scripts never depend on print

Logs help in:

Debugging

Audit

Compliance

History tracking

Example log:

2026-02-09 10:30:22 - INFO - Checking unused EBS volumes...

📧 Email Notification System
Why Email Is Needed

In companies:

Scripts run via cron / Jenkins

Nobody checks terminal output

Email alerts notify teams instantly

This project sends:

Stopped EC2 list

Unused EBS volumes

Unused Elastic IPs

Old snapshots

How Email Is Implemented

Used Gmail SMTP

Enabled 2FA

Generated App Password

Used smtplib and email.mime.text

Email subject:

AWS Cloud Report


Email body example:

Stopped EC2 instances:
i-0abc123
i-0xyz456

Unused EBS volumes:
vol-01234

🔐 Security Best Practices Used

Used Gmail App Password, not real password

No AWS secrets hard-coded

IAM permissions can be restricted to read-only

Script does not delete resources automatically

🧪 How to Run the Project

Configure AWS credentials:

aws configure


Install dependencies:

pip install boto3


Run script:

python main.py


Check:

Email inbox

Logs/aws_cleanup.log

🎯 What This Project Proves in Interviews

This project shows that I:

Understand AWS cost optimization

Can write real automation scripts

Know boto3 & AWS APIs

Use modular coding

Implement email alerts

Follow production DevOps practices
