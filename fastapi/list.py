import boto3
from fastapi import HTTPException, APIRouter

router = APIRouter()

s3= boto3.client('s3')
bucket_name = 'mybuckettest11'

@router.get("/files")
def list_files():
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' not in response:
            return {"message": "No files found"}
        files  = [obj['Key'] for obj in response['Contents']]
        return {'files': files}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))