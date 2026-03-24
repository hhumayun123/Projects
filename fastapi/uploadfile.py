import boto3
from fastapi import APIRouter, HTTPException, File, UploadFile

router =  APIRouter()

AWS_BUCKET_NAME = "mybuckettest11"
AWS_REGION = "us-east-1"

s3_client = boto3.client('s3', region_name = AWS_REGION)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        s3_client.upload_fileobj(file.file, AWS_BUCKET_NAME, file.filename)
        file_url = f"https://{AWS_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{file.filename}"
        return {"message": "File uploaded successfully", "file_url": file_url}
    except NoCredentialsError:
        raise HTTPException(status_code=500, detail="AWS credentials not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
