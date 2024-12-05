import os
import boto3
from flask import Flask, request, jsonify
from flask_cors import CORS
from botocore.exceptions import NoCredentialsError, ClientError
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv("SECRET_ID"),
    aws_secret_access_key=os.getenv("SECRET_KEY"),
    region_name='eu-north-1'
)

CORS(app)
BUCKET_NAME = "direct-upload-pdp"

@app.route('/generate-upload-url', methods=['POST'])
def generate_upload_url():
    file_name = request.json.get('file_name')  # Get the file name from the frontend
    if not file_name:
        return jsonify({"error": "File name is required"}), 400

    try:
        # Generate the pre-signed URL for the upload
        upload_url = s3_client.generate_presigned_url('put_object',
                                                      Params={'Bucket': BUCKET_NAME, 'Key': file_name},
                                                      ExpiresIn=3600)  # The URL expires in 1 hour
        return jsonify({"upload_url": upload_url})
    
    except NoCredentialsError:
        return jsonify({"error": "AWS credentials not found"}), 500
    except ClientError as e:
        # Log the actual error returned by AWS
        return jsonify({"error": str(e)}, 500)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)