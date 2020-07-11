from main import lambda_handler
import boto3
import json

from boto3.dynamodb.conditions import Key

def test_lambda_handler():
    test_results = json.dumps(lambda_handler({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'},{}))
    client = boto3.resource('dynamodb')
    table = client.Table('MyWebsiteTable')
    response = table.get_item(Key={'type': 'resume'})
    assert int(response['Item']['views'])==json.loads(test_results)['body']['views']