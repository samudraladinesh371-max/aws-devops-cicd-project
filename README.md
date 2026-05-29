Automated CI/CD Deployment Using Jenkins and Docker on AWS

Project Overview

This project demonstrates a complete CI/CD pipeline deployment using:

AWS EC2
Jenkins
Docker
GitHub
Python Flask Application
Terraform (Infrastructure Provisioning)

The pipeline automatically:

Pulls latest source code from GitHub
Builds a Docker image
Stops old container
Creates and runs a new container
Deploys the updated Flask application automatically

Architecture

Developer Pushes Code to GitHub
              ↓
        Jenkins Pipeline
              ↓
      Docker Image Build
              ↓
    Stop Old Running Container
              ↓
   Deploy New Docker Container
              ↓
 Flask Application Running on EC2

 Technologies Used

 | Technology   | Purpose                |
| ------------ | ---------------------- |
| AWS EC2      | Cloud Server Hosting   |
| Terraform    | Infrastructure as Code |
| Jenkins      | CI/CD Automation       |
| Docker       | Containerization       |
| Git & GitHub | Version Control        |
| Python Flask | Web Application        |
| Linux        | Server Environment     |

Project Structure

flask-devops-app/
│
├── devops-project/
│   ├── app.py
│   ├── Dockerfile
│   ├── Jenkinsfile
│   └── requirements.txt
│
└── README.md
