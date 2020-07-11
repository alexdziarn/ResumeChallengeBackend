import json
import boto3

from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    client = boto3.resource('dynamodb', region_name='us-east-1')
    table = client.Table('MyWebsiteTable')
    response = table.get_item(Key={'type': 'resume'})
    if "Item"not in response:
        table.put_item(
            Item={
                'type': 'resume',
                'views': 0
            }
        )
    response = table.get_item(Key={'type': 'resume'})
    table.update_item(
        Key={'type': 'resume'},
        UpdateExpression='SET #vw = :val1',
        ExpressionAttributeValues={
            ":val1": int(response['Item']['views']+1)
        },
        ExpressionAttributeNames={
            "#vw": "views"
        }
    )
    response = table.get_item(Key={'type': 'resume'})

    return{
        "statusCode": 200,
        "body": json.dumps({
            "views":int(response['Item']['views']),
        }),
        "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Methods': '*',
            'Access-Control-Allow-Origin': '*'
        }
    }