import boto3
from fastapi import APIRouter, HTTPException

router = APIRouter()

s3 = boto3.client('s3')
bucket_name = 'mybuckettest11'

@router.delete('/delete/{filename}')
def delete_file(filename: str):
    try:
       response = s3.delete_object(Bucket=bucket_name, Key=filename)
       if response.get('ResponseMetaData',{}).get('HTTPStatusCode') == 204:
           return {"message": "File deleted successfully"}
       else:
           return {"message": f"Delete request sent for '{filename}'"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
