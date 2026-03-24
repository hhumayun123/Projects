import boto3
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
import io

router = APIRouter()

s3 = boto3.client('s3')
bucket_name = 'mybuckettest11'


@router.get("/download/{filename}")
def downlaod_file(filename: str):
    if not filename:
        raise HTTPException(status_code=400, detail="Filename is required")
    try:
        file_obj = s3.get_object(Bucket=bucket_name, Key=filename)
        file_content = file_obj['Body'].read()

        stream = io.BytesIO(file_content)

        return StreamingResponse(stream, media_type="application/octet-stream", headers={"Content-Disposition": f"attachment; filename={filename}"})
    except  Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


