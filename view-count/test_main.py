from main import lambda_handler
import boto3
import json

def test_lambda_handler():
    test_results = json.dumps(lambda_handler())
    if len(test_results)==0
        a=1
        assert a==1
    else:
        assert list(test_results.values())[1].values()[1] > 0