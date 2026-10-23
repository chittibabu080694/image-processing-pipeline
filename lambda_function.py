import boto3
import os
from io import BytesIO
from PIL import Image

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Get the bucket name and key from the S3 event notification
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    image_key = event['Records'][0]['s3']['object']['key']
    
    # Define destination bucket (can be environment variable or hardcoded)
    destination_bucket = os.environ.get('DESTINATION_BUCKET', source_bucket)
    
    print(f"Processing image {image_key} from bucket {source_bucket}")
    
    # Download the image from S3
    response = s3_client.get_object(Bucket=source_bucket, Key=image_key)
    image_content = response['Body'].read()
    
    # Process the image using Pillow (e.g., resize to thumbnail 300x300)
    with Image.open(BytesIO(image_content)) as img:
        img.thumbnail((300, 300))
        
        # Save processed image to buffer
        buffer = BytesIO()
        file_format = img.format if img.format else 'JPEG'
        img.save(buffer, format=file_format)
        buffer.seek(0)
        
        # Define new path for processed image
        destination_key = f"processed/{image_key}"
        
        # Upload processed image back to S3
        s3_client.put_object(
            Bucket=destination_bucket,
            Key=destination_key,
            Body=buffer,
            ContentType=response['ContentType']
        )
        
    print(f"Successfully processed and uploaded: {destination_key}")
    return {
        'statusCode': 200,
        'body': f"Image {image_key} processed successfully!"
    }
