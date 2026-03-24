from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from uploadfile import router as upload_router
from list import router as list_router
from download import router as download_router
from delete import router as delete_router

app =FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(list_router)
app.include_router(download_router)
app.include_router(delete_router)

