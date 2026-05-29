import json

def lambda_handler(event, context):
    for record in event["Records"]:
        body = json.loads(record["body"])
        print(f"Processing event: {body['event_id']}")

    return {
        "statusCode": 200,
        "message": "Events processed"
    }
