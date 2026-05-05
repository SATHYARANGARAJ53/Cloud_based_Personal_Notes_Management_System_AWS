import boto3
import json
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

TABLE_NAME = 'notes_table'
BUCKET_NAME = 'personal-notes-53'   # replace with your exact bucket name

table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        # Fetch all notes from DynamoDB
        response = table.scan()
        notes = response['Items']

        # Convert notes to JSON
        backup_data = json.dumps(notes, indent=4)

        # Generate backup file name
        timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"backup_{timestamp}.json"

        # Upload backup JSON to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=backup_data
        )

        return {
            'statusCode': 200,
            'body': f"Backup successful: {file_name}"
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
