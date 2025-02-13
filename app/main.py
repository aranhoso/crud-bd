from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import logging
import sys
from fastapi.middleware.cors import CORSMiddleware

from . import models, schemas
from .database import engine, get_db

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Simple API",
    description="A simple API that returns 200 OK",
    version="1.0.0"
)

@app.get("/health")
async def health_check():
    """Endpoint específico para healthcheck"""
    return {"status": "healthy"}

@app.get("/", status_code=status.HTTP_200_OK)
def root():
    logger.info("Root endpoint called")
    return {"status": "success", "message": "API is running"}