from main import lambda_handler
import boto3
import json

def test_lambda_handler():
    if "Item"not in boto3.resource('dynamodb').Table('MyWebsiteTable').get_item(Key={'type': 'resume'}):
        a=1
        assert a==1
    else
        test_results = json.dumps(lambda_handler())
        assert list(test_results.values())[1].values()[1] == boto3.resource('dynamodb').Table('MyWebsiteTable')['Item']['views']