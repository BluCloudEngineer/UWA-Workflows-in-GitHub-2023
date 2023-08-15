# AWS CodePipeline Pipeline README

## Overview

This directory is not related to the Python Flask web application, but it includes the files required to create a CI / CD pipeline in AWS. Normally, you should keep software code and Infrastructure as Code (IoC) in separate repositories, but I have included them together for ease of simplicity.

If you want to use the AWS CloudFormation template, you will need to update line `310` in the `pipeline.yml` file to match your GitHub account and repository name.

## Assumptions

*   You will need an [Amazon Web Services](https://aws.amazon.com/) account.
*   All AWS resources used in this repository fall under the [AWS Free Tier](https://aws.amazon.com/free/), however, if you deploy this to your AWS account, you are responsible for **any / all** costs incurred.
*   You have already created a default Amazon S3 Bucket used by AWS CodePipeline.
*   You have already created the default IAM service role for AWS Elastic Beanstalk.
*   The Amazon EC2 web server(s) used by AWS Elastic Beanstalk will be deployed in the default VPC of your AWS account. If you are deploying this for a production environment, it is recommended to create a new VPC.
*   All AWS resources are deployed in the Asia Pacific (Sydney) ap-southeast-2 Region.
*   You have already created the connector between GitHub and AWS. More information can be found [here](https://docs.aws.amazon.com/codepipeline/latest/userguide/connections-github.html).

## Deploying the Pipeline

1.  Login to the AWS Management Console.

2.  Change your Region to `ap-southeast-2 (Sydney)` (if you haven't already).

3.  Navigate to the `AWS CloudFormation Console`.

4.  Create a new Stack with new resources (standard).

5.  Confirm that the `Template is ready` radio button is selected, select `Upload a template file` and upload the following file `pipeline/pipeline.yml`, then press `Next`.

6.  Enter the following for the `Stack name`: UWA-Workflows-in-GitHub-2023-Pipeline

7.  Enter the GitHub connector ARN for the `GitHubConnectionArn` parameter.

8.  Enter the name of the Amazon S3 bucket used by AWS CodePipeline for the `PipelineAmazonS3Bucket` parameter.

9.  Enter the name of the GitHub branch to trigger the pipeline for the `TargetBranch` parameter.

10. Press `Next`.

11. Press `Next` again.

12. Scroll down to the bottom of the page and select the `I acknowledge that AWS CloudFormation might create IAM resources` checkbox, then press `Submit`.

13. Once the pipeline stack has been deployed, it will automatically deploy the Python Flask web application to AWS.

14. Under the `Outputs` section of the newly created stack, you can access the URL endpoint of the Python Flask web application.
