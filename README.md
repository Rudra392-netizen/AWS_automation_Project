<h1 align="center">🚀 AWS Automation Using Boto3</h1>

<p align="center">
  <b>Python | AWS | Boto3 | DevOps Automation</b><br/>
  <i>Automating detection of unused AWS resources to improve cloud cost visibility</i>
</p>

<hr/>

<h2>📌 Project Overview</h2>

<p>
In AWS environments, cloud costs often increase due to unused resources such as
stopped EC2 instances, unattached EBS volumes, idle Elastic IPs, and old snapshots.
Manually checking these resources every day from the AWS Console is time-consuming
and error-prone.
</p>

<p>
To solve this problem, I built this <b>AWS Automation Using Boto3</b> project using
<b>Python</b>. This project automatically scans AWS resources, identifies unused
components, logs the results, and sends a summary report via email.
</p>

<p>
The project focuses on <b>safe detection and reporting</b>, not deletion, which makes
it suitable for real production environments.
</p>

<hr/>

<h2>🎯 Why I Built This Project</h2>

<ul>
  <li>To understand real-world AWS cost optimization problems</li>
  <li>To automate daily AWS monitoring tasks</li>
  <li>To gain hands-on experience with Boto3</li>
  <li>To build a strong DevOps portfolio project</li>
  <li>To avoid manual AWS Console dependency</li>
</ul>

<hr/>

<h2>🛠️ Technologies Used</h2>

<ul>
  <li><b>Python 3</b></li>
  <li><b>AWS Boto3 SDK</b></li>
  <li><b>AWS EC2, EBS, Elastic IP, Snapshots</b></li>
  <li><b>SMTP Email Notification</b></li>
  <li><b>Python Logging Module</b></li>
</ul>

<hr/>

<h2>📂 Project Structure</h2>

<pre>
aws_automation_using_Boto3/
│
├── main.py
├── Logs/
│   └── aws_cleanup.log
│
└── services/
    ├── ec2_cleanup.py
    ├── ebs_cleanup.py
    ├── eip_cleanup.py
    └── snapshot_cleanup.py
</pre>

<hr/>

<h2>⚙️ How the Project Works</h2>

<ol>
  <li>The <code>main.py</code> file acts as the entry point</li>
  <li>Each AWS service logic is separated inside the <code>services</code> folder</li>
  <li>Python lists are used to collect unused resources dynamically</li>
  <li><code>.append()</code> is used to store results as the scan progresses</li>
  <li>All results are logged inside the <code>Logs</code> directory</li>
  <li>A summary email is sent after execution</li>
</ol>

<hr/>

<h2>🔍 AWS Services Covered</h2>

<h3>🖥️ EC2 Instances</h3>
<ul>
  <li>Detects stopped EC2 instances</li>
  <li>Helps identify unused compute resources</li>
</ul>

<h3>💾 EBS Volumes</h3>
<ul>
  <li>Finds unattached EBS volumes</li>
  <li>Prevents paying for unused storage</li>
</ul>

<h3>🌐 Elastic IPs</h3>
<ul>
  <li>Detects Elastic IPs not associated with any instance</li>
  <li>AWS charges for idle Elastic IPs</li>
</ul>

<h3>📸 Snapshots</h3>
<ul>
  <li>Lists old or unused snapshots</li>
  <li>Useful for manual cleanup decisions</li>
</ul>

<hr/>

<h2>📧 Email Notification Implementation</h2>

<ul>
  <li>Email is sent automatically after script execution</li>
  <li>Contains a summary of all unused resources</li>
  <li>Implemented using SMTP</li>
  <li>Uses Gmail App Password (2FA enabled)</li>
  <li>No credentials are hardcoded in plain text</li>
</ul>

<hr/>

<h2>📜 Logging Mechanism</h2>

<ul>
  <li>Uses Python <code>logging</code> module</li>
  <li>Logs stored inside <code>Logs/aws_cleanup.log</code></li>
  <li>Helps in auditing and debugging</li>
</ul>

<hr/>

<h2>🔐 Security Considerations</h2>

<ul>
  <li>No destructive AWS actions performed</li>
  <li>IAM user with limited permissions</li>
  <li>No AWS keys stored in code</li>
  <li>Email authentication via App Password</li>
</ul>

<hr/>

<h2>▶️ How to Run the Project</h2>

<ol>
  <li>Configure AWS credentials on your system</li>
  <li>Enable Gmail 2FA and create an App Password</li>
  <li>Update email configuration inside the script</li>
  <li>Run the project:
    <pre>python main.py</pre>
  </li>
</ol>

<hr/>

<h2>🚀 Why This Project Is Interview-Ready</h2>

<ul>
  <li>Real-world AWS cost optimization use case</li>
  <li>Clean project structure</li>
  <li>Safe automation design</li>
  <li>Demonstrates Python + AWS integration</li>
  <li>Production mindset (logging + alerts)</li>
</ul>

<hr/>

<h2>📈 Future Enhancements</h2>

<ul>
  <li>Jenkins scheduled execution</li>
  <li>AWS Lambda deployment</li>
  <li>Slack or SNS notifications</li>
  <li>Approval-based automated cleanup</li>
</ul>

<hr/>

<h2>📄 License</h2>

<p>
This project is licensed under the <b>MIT License</b>.
You are free to use, modify, and distribute this project for learning and development purposes.
</p>

<hr/>

<p align="center">
<b>⭐ If you like this project, feel free to star the repository ⭐</b>
</p>
