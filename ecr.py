import boto3
from botocore.exceptions import ClientError

ecr_client = boto3.client('ecr', region_name='us-east-1')
repository_name = 'pavan_rep'

try:
    # Attempt to create the repository
    response = ecr_client.create_repository(repositoryName=repository_name)
    repository_uri = response['repository']['repositoryUri']
    print(f"Repository URI: {repository_uri}")
except ClientError as e:
    # Handle any error that occurs
    print(f"An error occurred: {e}")
