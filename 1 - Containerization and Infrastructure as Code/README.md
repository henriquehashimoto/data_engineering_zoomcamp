# Week 1: Introduction & Prerequisites

**Tech**

- Docker
- Postgres
- Google Cloud Platform (GCP)
- Terraform

**Focus:** Week 1 is dedicated to setting up the key tools and technologies you’ll be using throughout the course.

**Local Part:** Learn to package your application and its dependencies with Docker and run a fully functioning database using PostgreSQL.

**Cloud Part:** Discover Google Cloud Platform and Terraform, focusing on automating the setup and management of your cloud architecture.


# DOCKER
The fastest way to containerize applications.
Docker Desktop is secure, out-of-the-box containerization software offering developers and teams a robust, hybrid toolkit to build, share, and run applications anywhere.

## Why we should care about docker

- Local experiments
- Integration test (CI/CD)
- Reproducibility
- Running pipelines on the cloud (AWS Batch, BQC, Kurbenets Jobs)   
- Spark
- Serverless (AWS Lambda, Google functions)


## Using Docker
After the installation it can be used by cmd or bash 

### Starting Docker
`docker run -it --entrypoint=bash python:3.9`
- This will create a new container with python 3.9. After that, we can use just like normal python, installing libraries and programming 

`docker build -t test:pandas .`
- Creating a docker image on the current folder; need a "dockerfile" created with instructions.
- Name of the image that will be used: test

