from src.lambda_handler import lambda_handler

def test_lambda_handler():
    event = {
        "Records": [
            {
                "body": '{"event_id":"123"}'
            }
        ]
    }

    result = lambda_handler(event, None)

    assert result["statusCode"] == 200
