# Cloud-Based Personal Notes Management System AWS

## 📌 Project Goal
The goal of this project is to develop a cloud-enabled personal notes management application that allows users to create, view, update, and delete notes efficiently while ensuring secure cloud storage and automated backup of data. The project demonstrates the integration of multiple AWS services with Python to build a scalable and reliable cloud application.

---

## 📖 About the Project
The Cloud-Based Personal Notes Management System is a terminal-based application deployed on an Amazon EC2 instance. It enables users to manage personal notes through CRUD operations, with all note records stored in Amazon DynamoDB for fast and flexible NoSQL storage.

To ensure data durability and cloud automation, AWS Lambda is used to periodically fetch all notes from DynamoDB and generate backup snapshots in JSON format, which are stored in Amazon S3. Amazon EventBridge triggers the Lambda function automatically at scheduled intervals, making the system fully backed up without manual intervention.

This project combines cloud hosting, serverless automation, database management, and object storage into a single practical application.

---

## ✨ Key Features
- Create new personal notes with title and content
- View all saved notes
- Update existing notes
- Delete unwanted notes
- Cloud-hosted execution using Amazon EC2
- Real-time note storage in Amazon DynamoDB
- Automated scheduled backup using AWS Lambda
- JSON backup archive stored in Amazon S3
- EventBridge scheduling for periodic automation
- Secure IAM role-based AWS resource access

---

## 🛠 Tech Stack Used

- **Amazon EC2** – Cloud-based virtual server used to deploy and run the Python personal notes management application.

- **Amazon DynamoDB** – NoSQL database service used to store all note information including note ID, title, content, and creation time.

- **AWS Lambda** – Serverless compute service used to automatically process and back up notes data without manual intervention.

- **Amazon S3** – Object storage service used to maintain periodic JSON backup files of all stored notes.

- **Amazon EventBridge** – Scheduling service used to trigger the Lambda backup function at regular time intervals.

- **AWS IAM** – Identity and Access Management service used to securely control permissions and communication between AWS resources.
  
---

## 📚 What I Gained From This Project
Through this project, I gained practical hands-on experience in:
- launching and configuring EC2 Ubuntu instances,
- connecting Python applications with DynamoDB using boto3,
- writing CRUD-based cloud applications,
- creating AWS Lambda functions for automated processing,
- storing structured backup files in Amazon S3,
- configuring EventBridge scheduled triggers,
- handling IAM role permissions between AWS services,
- and understanding end-to-end cloud application architecture.

This project significantly strengthened my understanding of AWS cloud service integration with Python.

---

## ✅ Project Workflow
User interacts with Python Notes Application on EC2  
→ Notes stored in DynamoDB  
→ EventBridge triggers Lambda every scheduled interval  
→ Lambda reads all notes from DynamoDB  
→ Backup JSON file generated  
→ Backup stored securely in S3 bucket
