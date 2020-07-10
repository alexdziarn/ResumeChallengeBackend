from main import lambda_handler
import boto3
import json

def test_lambda_handler():
    test_results = json.dumps(lambda_handler())
    if test_results==0:
        a=2
        assert a==2
    else:
        assert list(test_results.values())[1].values()[1] > 0