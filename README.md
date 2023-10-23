# CI/CD pipeline with GCP
This repository contains a simple Flask application to demonstrate the use of Cloud Build in a CI/CD pipeline. Cloud Build is a service that can be used to build, test and deploy to Google Cloud. We will look at a simple pipeline that utilizes Github, Cloud Build, Container Registry and Cloud Run.

## Creating the cloudbuild.yaml file
First, we specify the steps for Cloud Build in cloudbuild.yaml

```
steps:
# Build the container image
- name: gcr.io/cloud-builders/docker
  args: ['build', '-t', 'gcr.io/$PROJECT_ID/${_SERVICE_NAME}:${SHORT_SHA}', '.']
  id: Building the container image
# Push the container image to Container Registry
- name: 'gcr.io/cloud-builders/docker'
  args: ['push', 'gcr.io/$PROJECT_ID/${_SERVICE_NAME}:${SHORT_SHA}']
  id: Pushing the image to registry
# Deploy container image to Cloud Run
- name: 'gcr.io/cloud-builders/gcloud'
  args: ['run', 'deploy', '${_SERVICE_NAME}', '--image', 'gcr.io/$PROJECT_ID/${_SERVICE_NAME}:${SHORT_SHA}', '--region', 'asia-east1', '--platform', 'managed', "--allow-unauthenticated"]
```

## Enable APIs in the Cloud Project
Firstly, enable the Cloud Build API and Cloud Run API

## Connecting the repository and creating a trigger
Next, select and connect a source code management provider (Github, Bitbucket) to Cloud Build and select your desired repository

![image](https://github.com/AshKetchup38/cicd-demo/assets/135846103/2c9e49bc-ba22-44d9-b1ab-56b122057a12)

Create a trigger that will be invoked every time code is pushed to a specific branch or all branches. Ensure that the configuration type is selected as "Cloud Build configuration file" and the file path is correct. Also ensure that a variable "_SERVICE_NAME" is added.

![image](https://github.com/AshKetchup38/cicd-demo/assets/135846103/ceb12f4f-ae79-4a24-8852-8bb0793bbfb1)

Lastly, ensure that the service account permissions for Cloud Run Admin and Service Account User are enabled

![image](https://github.com/AshKetchup38/cicd-demo/assets/135846103/cc372cc6-5aa2-4a9a-bd45-8dcaa966e867)

## Commit changes to the repository and view build results
Pushing code to the repository should trigger cloud build and the build results will be shown in the Build History menu

![image](https://github.com/AshKetchup38/cicd-demo/assets/135846103/ff9cc38f-37b0-406e-b4fa-564575d4a6b3)


