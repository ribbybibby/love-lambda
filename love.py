from botocore.vendored import requests
import os
import boto3

def lambda_handler(event, context):
    arn = os.environ["SNS_ARN"]
    
    r = requests.get('https://quotes.rest/qod', params={'category':'love'})

    data = r.json()

    if data["success"]["total"] > 0:
        quote = data["contents"]["quotes"][0]

        client = boto3.client('sns')
        r = client.publish(
            TopicArn=arn,
            Message='"'+quote["quote"]+'" - '+quote["author"]
        )
    else:
        raise Exception('Issue retrieving quote from the API!')