from main import lambda_handler

def test_lambda_handler():
    result = lambda_handler()
    assert result is not None